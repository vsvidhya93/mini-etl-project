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

Name	Email	Department	Salary
 Allison Hill 	jillrhodes@miller.com		50000
Lance Hoffman			50000
Melinda Jones	FRANKGRAY@WATTS.COM	IT	


After Cleaning:

Name	Email	Department	Salary
Allison Hill	jillrhodes@miller.com	Not Assigned	50000
Lance Hoffman	Unknown	Not Assigned	50000
Melinda Jones	frankgray@watts.com	IT	55000


## Log File

2025-05-16 17:27:18,107 - root - INFO - Input File Moved Successfully to Source folder!
2025-05-16 17:27:18,118 - root - INFO - Removed duplicate records
2025-05-16 17:27:18,122 - root - INFO - Removed empty records without employee Name
2025-05-16 17:27:23,005 - root - INFO - checked for valid email address
2025-05-16 17:27:23,008 - root - INFO - Handled empty email and department columns with valid data
2025-05-16 17:27:23,009 - root - INFO - Converted salary column to numeric
2025-05-16 17:27:23,011 - root - INFO - Filled empty salary records with median 
2025-05-16 17:27:23,017 - root - INFO - Number of records excluding header : 52
2025-05-16 17:27:23,019 - root - INFO - Number of duplicate records removed: 3
2025-05-16 17:27:23,019 - root - INFO - Number of unique records : 49
2025-05-16 17:27:23,019 - root - INFO - Removed 3 records without employee name successfully!
2025-05-16 17:27:23,019 - root - INFO - Final number of records excluding header: 46
2025-05-16 17:27:23,019 - root - INFO - Cleansed employee data written to CSV
2025-05-16 17:27:23,022 - root - INFO - Output File Moved Successfully to Target Folder!



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


## 🚀 How to Run
```bash
python EmployeeETL.py

