# Task 3: List Comprehensions

import csv

# Reading the CSV file and creating a list of employee full names
with open("./csv/employees.csv", "r") as csvfile:
    reading = csv.reader(csvfile)

    rows = list(reading)
# Creating a list of full names (first name + last name)
employee_list = [row[1] + " " + row[2] for row in rows[1:]]
print(employee_list)

# Creating a list of names that contain the letter 'e'
only_e = [name for name in employee_list if "e" in name]
print(only_e)
