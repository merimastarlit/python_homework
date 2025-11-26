# TASK 2
# %%
from datetime import datetime
import csv
import os
import custom_module


def read_employees():
    our_dict = {}
    our_list = []
    try:
        with open("./csv/employees.csv", "r") as csvfile:
            reader = csv.reader(csvfile)

            # creating dictionary and list from csv file
            for index, row in enumerate(reader):
                if index == 0:
                    our_dict["fields"] = row
                else:
                    our_list.append(row)
                    our_dict["rows"] = our_list
    # addressing possible exceptions
    except SyntaxError:
        print("There is a syntax error in the code.")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return our_dict


# calling the function
employees = read_employees()
print(employees)


# %%

# TASK 3

# %%

def column_index(column_name):
    # finding the index of the given column name
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")

# TASK 4
# %%


def first_name(row_number):
    # first getting the first name of the employee at the given row number
    index = column_index("first_name")
    # getting the row at the given row number
    row = employees["rows"][row_number]
    #  returning the first name from that row
    return row[index]


# TASK 5
# %%


def employee_find(employee_id):
    # defining a helper function to match employee_id
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    # filtering the rows using the helper function
    matches = list(filter(employee_match, employees["rows"]))

    return matches


# %%

# TASK 6

def employee_find_2(employee_id):
    # filtering the rows using a lambda function
    matches = list(filter(lambda row: int(
        row[employee_id_column]) == employee_id, employees["rows"]))

    return matches

# TASK 7


def sort_by_last_name():
    # sorting the employees by last name using the column index
    sorted_list = employees["rows"].sort(
        key=lambda row: column_index("last_name"))
    return sorted_list


print(sort_by_last_name())


# TASK 8
# %%

def employee_dict(row):
    # creating a dictionary for an employee from a row of data
    # skip employee_id at index 0
    fields = employees["fields"][1:]
    # also skip employee_id in the row
    values = row[1:]
    # making a dict from field:value pairs
    return dict(zip(fields, values))


print(employee_dict(employees["rows"][1]))


# TASK 9

def all_employees_dict():
    # empty dict to hold all employees
    dict_of_dicts = {}
    # populating the dict with employee_id as key and employee_dict as value
    for row in employees["rows"]:
        employee_id = int(row[employee_id_column])
        dict_of_dicts[employee_id] = employee_dict(row)

    return dict_of_dicts


# global variable to hold all employees dict
all_employees = all_employees_dict()
print(all_employees)

# TASK 10


def get_this_value():
    # getting the environment variable THISVALUE
    get_my_env = os.getenv('THISVALUE')
    return get_my_env


print(get_this_value())

# TASK 11


def set_that_secret(new_secret):
    # setting the secret in custom_module
    custom_module.set_secret(new_secret)


set_that_secret("example")

print(custom_module.secret)

# TASK 12
# %%


def read_minutes():
    # reading two csv files and storing their contents in dictionaries
    minutes1 = {"fields": [], "rows": []}
    minutes2 = {"fields": [], "rows": []}

    try:
        with open("./csv/minutes1.csv", "r") as file1, open("./csv/minutes2.csv", "r") as file2:
            reader1 = csv.reader(file1)
            for index, row in enumerate(reader1):
                if index == 0:
                    minutes1["fields"] = row
                else:
                    # ✅ add each row as a tuple
                    minutes1["rows"].append(tuple(row))

            reader2 = csv.reader(file2)
            for index, row in enumerate(reader2):
                if index == 0:
                    minutes2["fields"] = row
                else:
                    minutes2["rows"].append(tuple(row))

    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print("Minutes 1:")
print(minutes1)

print("\nMinutes 2:")
print(minutes2)


# TASK 13
# %%
def create_minutes_set():
    # creating a set of unique minutes from both files
    first_set = set(minutes1["rows"])
    second_set = set(minutes2["rows"])
    # combining the two sets to get unique minutes
    combined_set = first_set.union(second_set)

    return combined_set


# setting a global variable for minutes_set to be used later
minutes_set = create_minutes_set()
print(minutes_set)


# %%
# TASK 14


def create_minutes_list():
    # converting the set of unique minutes to a list
    list_version = list(minutes_set)
    # converting the date strings to datetime objects
    mapped = map(lambda x: (x[0], datetime.strptime(
        x[1], "%B %d, %Y")), list_version)

    return list(mapped)


# global variable for minutes_list to be used later
minutes_list = create_minutes_list()
print(minutes_list)


# TASK 15
# %%


def write_sorted_list():
    # Sorting minutes_list by date (index 1)
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    # Converting datetime object back to string
    converted = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))

    # Writing to CSV file
    with open("./minutes.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)

    return converted


written_minutes = write_sorted_list()
print(written_minutes)

# %%
