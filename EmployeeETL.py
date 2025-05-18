#import re
import pandas as pd
import logging
import datetime
import os, shutil
from email_validator import validate_email, EmailNotValidError

#Define the log filename and get the input file name from user
log_filename = f"Logs\\EmployeeETL_{datetime.date.today()}.log"
input_filename = input("Enter the file name : ")
input_folder = 'C:\\Users\\vsvid\\PycharmProjects\\EmployeeDetails\\Input'

#Define the log level and format
logging.basicConfig(filename=log_filename, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#Moving input file to source folder
if os.path.exists(input_filename):
    if os.path.exists(f'{input_folder}\\{input_filename}'):
        os.remove(f'{input_folder}\\{input_filename}')
        shutil.move(input_filename, input_folder)
        logging.info("Input File Moved Successfully to Source folder!")
    else:
        shutil.move(input_filename, input_folder)
        logging.info("Input File Moved Successfully to Source folder!")
else:
        logging.error("File Not Found")

#Reading input file
try:
    data = pd.read_csv(f'{input_folder}\\{input_filename}')
    NumOfRecords = len(data) - 1  #53-1=52

    #Removing the duplicate records
    data.drop_duplicates(inplace=True)
    logging.info("Removed duplicate records")

    #Removing records without the key column
    unique_records = len(data) - 1  #50-1=49
    data['Name'] = data['Name'].str.strip()
    data.dropna(subset='Name', inplace=True)
    logging.info("Removed empty records without employee Name")

    #Checking if the email is valid
    RemainingRecords = (len(data) - 1)
    data['Email'] = data['Email'].str.lower()
    data['Email'] = data['Email'].str.strip()


    def is_validemail(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            #logging.error("Email is not valid")
            return False


    data['Email'] = data['Email'].apply(lambda x: x if is_validemail(str(x)) else None)
    #data['Email']=data['Email'].apply(lambda x:x if bool(re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',x)) else None)
    logging.info("checked for valid email address")

    #Handling null values for email and department columns
    data.fillna({'Email': 'Unknown', 'Department': 'Not Assigned'}, inplace=True)
    logging.info("Handled empty email and department columns with valid data")

    #converting salary column to numeric and replacing null values with median of salary
    try:
        data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')
        logging.info("Converted salary column to numeric")
    except ValueError:
        logging.error(f"The salary column is not numeric")

    data['Salary'] = data['Salary'].apply(lambda x: None if x < 0 else x)
    data.fillna({'Salary': data['Salary'].median()}, inplace=True)
    logging.info(f"Filled empty salary records with median ")
    output_folder = 'C:\\Users\\vsvid\\PycharmProjects\\EmployeeDetails\\Output'
    output_filename = 'Employee_Cleaned.csv'
    #writing cleaned output to a csv file and logging summary information
    data.to_csv(f'{output_folder}\\{output_filename}', index=False)
    logging.info("Cleansed employee data written to output folder")
    logging.info(f"Number of records excluding header : {NumOfRecords}")
    logging.info(f"Number of duplicate records removed: {NumOfRecords - unique_records}")
    logging.info(f"Number of unique records : {unique_records}")
    logging.info(f"Removed {unique_records - RemainingRecords} records without employee name successfully!")
    logging.info(f"Final number of records excluding header: {len(data) - 1}")



except FileNotFoundError:
    logging.error("Input File Not Found")

except Exception as e:
    logging.error("Error Occured: %s", str(e))
