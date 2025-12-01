# 
# TASK 1
#%%
import traceback

try:
    with open("diary.txt", "a") as file:
        #first looping only
        first_time = True

        while True:
            if first_time:
                line = input("What happened today? ")
                #finish the first loop
                first_time = False
            else:
                line = input("What else? ")

            # writing the line to the file in a new line
            file.write(line + "\n")
            # checking if the user input exactly done for now. If so, break the loop
            if line.strip().lower() == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")






