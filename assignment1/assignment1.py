# Write your code here.

###
# Task 1
###

# %%
from statistics import mean


def hello():
    print("hello!")


hello()

# Task 2

# %%


def greet(name):
    print(f"Hello, {name}!")


greet("James")


# Task 3
# %%
def calc(num1, num2, operation="multiply"):
    try:
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "modulus":
                return num1 % num2
            case "divide":
                if num2 != 0:
                    return num1 / num2
    except Exception as e:
        return "You can't divide by 0"


print(calc(4, 2, "divide"))


"""# Task 4 """
# %%
#Task 4

def data_type_conversion(value, data_type):
    try:
        if data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
    except Exception as e:
        print(f"You can't convert {value} into a {type}")


print(data_type_conversion(12, "str"))


# Task 5
# %%
def grade(*args):

    try:
        # calculate the average
        total_sum = sum(args)
        num_args = len(args)
        average = total_sum / num_args

        # determine the grade based on average
        if average < 60:
            print(f"your grade is F")
        elif (60 <= average <= 69):
            print(f"your grade is D")
        elif (70 <= average <= 79):
            print(f"your grade is C")
        elif (80 <= average <= 89):
            print(f"your grade is B")
        elif average > 90:
            print(f"your grade is A")
    # handle if input was provided with wrong type
    except TypeError as e:
        print("Invalid data was provided.")


# call the function
grade(85, 78, 80)
grade("50")


# %%

# Task 6
# %%
def repeat(str, count):
    # initializing an empty string
    str = ''
    # loop to repeat the string
    for i in range(count):
        str += "hello,"
    print(str, end='')


repeat("hello", 5)
# %%
# Task 7


def student_scores(score, **kwargs):
    # checking if score is best or mean
    if score == "best":
        # finding the student with the highest score
        return max(kwargs, key=kwargs.get)
    # finding the student with the average score
    elif score == "mean":
        return mean(kwargs.values())


print(student_scores("best", Alice=90))

# Task 8
# %%


def titleize(phrase):
    # spliting the phrase into words
    words = phrase.split()
    # creating a new list to store the modified words
    new_words = []
    # loop through each word with its index
    for i, word in enumerate(words):
        # capitalizing the first and last word
        if i == 0 or i == len(words)-1:
            word = word.capitalize()
        # capitalizing words not in the exclusion list
        if word not in ["a", "on", "an", "the", "of", "and", "is", "in"]:
            word = word.capitalize()
        # adding the modified word to the new list
        new_words.append(word)
    #  return the joined list
    return " ".join(new_words)


print(titleize("how to be a billionaire"))

# Task 9
# %%


def hangman(secret, guess):
    # initializing an empty string to store the result
    result = ""
    # loop through each letter in secret word
    for letter in secret:
        if letter in guess:
            # if correct guess, add the letter to result
            result += letter
        else:
            # if incorrect guess, add underscore
            result += "_"
    return result


print(hangman("alphabet", "e"))


# Task 10

# %%

def pig_latin(words):
    # we need first split the words by space
    splitted_words = words.split(" ")
    # newly returned list
    added = []
    # loop through to find the first vowel
    for word in splitted_words:
        if word[0] in ["a", "e", "i", "o", "u"]:
            # after finding add it to the new list
            added.append(word + "ay")
        # resolve qu case
        elif word[:2] == "qu":
            added.append(word[2:] + "quay")
        else:
            # consonant case
            for i, letter in enumerate(word):
                if letter in ["a", "e", "i", "o", "u"]:
                    added.append(word[i:] + word[:i] + "ay")
                    # break after finding the first vowel
                    break
    # return the joined list
    return " ".join(added)


print(pig_latin("banana apple queue"))

# %%
