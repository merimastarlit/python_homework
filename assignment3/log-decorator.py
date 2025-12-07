# Task 1:

#%%
import logging
# Set up logger
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def log_decorator(func):
    # The decorator function
    def wrapper(*args, **kwargs):

        logger.log(logging.INFO, func.__name__)
        logger.log(logging.INFO, "positional parameters: %s",
                   args if args else "none")
        logger.log(logging.INFO, "keyword parameters: %s",
                   kwargs if kwargs else "none")

        result = func(*args, **kwargs)
        logger.log(logging.INFO, "return: %s", result)
        return result
    return wrapper

#using the decorator
@log_decorator
def greet(name, greeting="Hello"):
       return f"{greeting}, {name}!"       
       print("Hello, world!", end="\n\n")
# %%
