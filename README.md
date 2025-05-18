# Mini ETL Project

## 📋 Project Overview
This is a simple ETL (Extract-Transform-Load) project built with Python. The goal is to read employee data from a CSV file, clean and transform the data, and save the cleaned version for downstream use.

## 🔧 Technologies Used
- Python 3
- pandas
- logging
- email-validator
- datetime
- csv
- os / shutil (file operations)

## 🔄 ETL Flow

### 1. Extract
- Source file: `employees_dirty.csv` (contains raw employee data with missing values, duplicates, and formatting issues)

### 2. Transform
- Strip whitespace from text columns
- Convert email addresses to lowercase
- Remove rows with missing employee names
- Drop duplicate rows
- Handle missing values
- Convert salary to numeric and fill empty salary with median

### 3. Load
- Cleaned data is saved to `Employee_Cleaned.csv`
- Create log files with dates which contain all the summary and load information

## 📝 Example

Before cleaning:

![image](https://github.com/user-attachments/assets/5a69d9db-9dad-4338-a0e6-9d95bafed46d)

After cleaning:

![image](https://github.com/user-attachments/assets/72793a96-4079-459e-b0f1-da52bca33884)

## Log file

![image](https://github.com/user-attachments/assets/3e6c2ca1-4f77-4003-b5b2-daa45a0e4f1f)


##  Project Structure
mini-etl-project/
├── EmployeeETL.py
├── Input/
│ └── employees_dirty.csv
├── Output/
│ └── Employee_Cleaned.csv
├── Logs/
│ └── EmployeeETL_YYYY-MM-DD.log
└── README.md


