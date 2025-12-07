# Task 2:
#%%
# A decorator that converts the output of a function to a specified type
def type_converter(type_of_output):
    def converting_function(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return converting_function

#using the decorator
@type_converter(str)
def return_int():
    return 5

# another example
@type_converter(int)
def return_str():
    return "not a number"

# trying out the decorated function and handling exceptions
y = return_int()
# This should print "str"
print(type(y).__name__)  
try:
    y = return_str()
    print("shouldn't get here!")
except ValueError:
    # This is what should happen
    print("can't convert that string to an integer!")

# %%
