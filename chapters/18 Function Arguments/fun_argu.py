# Function Argument and return statement
# There are four types of argument that we can provide in a function

# Default argument
# Keyword argument
# Variable length argument
# Required argument

'''Basic example of Function'''
# def average(a,b):
#     print("The average is ", (a+b)/2)

# average(4,6)

'''Default Argument'''
'''We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.'''
# def average(a=8,b=1):
#     print("Average : ",(a+b)/2)
# # average()  
# average(3,4) 
# '''This will ignore 8 and 1 and it will cnoside 3 and 4 as new arguments'''
# average(3) '''now a will be considered as 3 and b will be default as 1''' 
# average(b=4) '''now b will be considered as 4 and a will be default as 8''' 


# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy","WIll")




'''Keyword arguments'''
'''We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.'''

# def name(fname, mname, lname):
#     print("Hello,", lname, fname, mname)

# name(mname = "Kishor", lname = "Sonawane", fname = "Jayesh")



'''Required Arguments'''
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

# Example
''' when number of arguments passed does not match to the actual function definition'''
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Quill")

# name("Peter", "Quill")\
# TypeError: name() missing 1 required positional argument: 'lname'

# Example 2
'''when number of arguments passed matches to the actual function definition.'''
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Ego", "Quill")

# Output
# Hello, Peter Ego Quill




'''Variable-length arguments:'''
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
'''There are two ways to achieve this:'''

#  1.Arbitrary Arguments:
'''While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.'''

# def name(*name):
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")

# output
# Hello, James Buchanan Barnes


# Example
# def average(*numbers):
#     sum =0
#     for i in numbers:
#         sum = sum +i
#     print("Average is : ",(sum/len(numbers)))

# average(5,6,7,8,9)


# 2. Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

# output
# Hello, James Buchanan Barnes









'''Return Statement'''
'''The return statement is used to return the value of the expression back to the calling function.'''
# def name(fname, mname, lname):
#     return "Hello, " + fname + " " + mname + " " + lname

# print(name("James", "Buchanan", "Barnes"))