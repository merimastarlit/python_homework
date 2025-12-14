# TASK 1: Creating and Manipulating DataFrames

import pandas as pd
import json
import numpy as np


# the data to include in the file

task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

print(task1_data_frame)

# a copy of the data
task1_with_salary = task1_data_frame.copy()

# adding more data
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

# another copy of the data
task1_older = task1_with_salary.copy()

# incrementing age by 1
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# saving the DataFrame to a CSV file
task1_older.to_csv("employees.csv", index=False)

print("DataFrame saved to employees.csv")


# TASK 2: Loading Data from CSV and JSON

# reading data from a csv file

task2_employees = pd.read_csv('employees.csv', sep=',')
print(task2_employees.head())

# creating a dataframe to save in a json file

additional_emloyees_df = pd.DataFrame({
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]

})

# saving it
additional_emloyees_df.to_json('additional_employees.json', orient='records')

# reading the json file
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# combining the two data files

more_employees = pd.concat(
    [task2_employees, json_employees], ignore_index=True)
print(more_employees)


# TASK 3: Data Inspection - Using Head, Tail, and Info Methods

# 3.1 the first three rows printed out
first_three = more_employees.head(3)
print(first_three)

# 3.2 the last two rows shown
last_two = more_employees.tail(2)
print(last_two)

# 3.3 get the shape of the Dataframe

employee_shape = more_employees.shape
print(employee_shape)

# 3.4 get the info of the Dataframe
more_employees.info()


# TASK 4: Data Cleaning - Handling Missing Values

# 4.1 creating a DataFrame from darty data csv
dirty_data = pd.read_csv("./assignment4/dirty_data.csv")
print(dirty_data)

#  creating a copy of the data
clean_data = dirty_data.copy()

# 4.2 removing any duplicate rows
clean_data = clean_data.drop_duplicates()
print(clean_data)


# 4.3 converting Age to numeric and handling missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# 4.4 replacing missing values in Salary with NaN
placeholders = ['Unknown', 'na']
clean_data['Salary'] = pd.to_numeric(
    clean_data['Salary'].replace(placeholders, np.nan), errors='coerce')

# 4.5 filling missing values with mean and median
mean_score = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_score)
print(clean_data['Age'])

median_score = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_score)

print(clean_data['Salary'])

# 4.6 converting hiring dates to Datetime

clean_data['Hire Date'] = pd.to_datetime(
    clean_data['Hire Date'], errors="coerce")
print(clean_data['Hire Date'])

# 4.7 stripping whitespace from Name and Department column
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip()

# standardizing with uppercase
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Department'] = clean_data['Department'].str.upper()

print(clean_data['Name'])
print(clean_data['Department'])
