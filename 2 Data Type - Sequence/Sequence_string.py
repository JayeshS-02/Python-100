'''
The sequence Data Type in Python is the ordered collection of similar or different Python data types. Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence data types of Python:

Python String
Python List
Python Tuple
'''
# Creating String
# Strings in Python can be created using single quotes, double quotes, or even triple quotes.

String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1))

String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))

String1 = '''Geeks 
            For 
            Life'''
print("\nCreating a multiline String: ")
print(String1)


# Accessing elements of String

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

print("\nFirst character of String is: ")
print(String1[0])

print("\nLast character of String is: ")
print(String1[-1])
