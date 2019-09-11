'''
squared.py - simple input-process-out example
'''
mynum = input("enter a number (e.g., 7): ") # get user input as string
mynum_int = int(mynum) # cast string to integer for math expression
mynum_output = mynum_int * mynum_int # assign value of math expression to new variable
mynum_str = str(mynum_output) # cast integer to a string for output using print() function
print("Your answer is " + mynum_str) # output answer to screen using print()
