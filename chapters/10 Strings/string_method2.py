# Strings are immutable

#  Every string method in Python does not change the original string instead returns a new string with the changed attributes. 

# Python3 program to show the 
# working of upper() function 
text = 'geeKs For geEkS'

# Length of string
print("Length of string : ", len(text))

# upper() function to convert 
# string to upper case 
print("Uppercase String:") 
print(text.upper()) 

# lower() function to convert 
# string to lower case 
print("lowercase String:") 
print(text.lower()) 

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String: first character to upper case and rest to lower case : ") 
print(text.title()) 

# swaps the case of all characters in the string 
# upper case character to lowercase and viceversa 
print("\Swap Case String:") 
print(text.swapcase()) 

# convert the first character of a string to uppercase 
print("\Capitalize String: first character of a string to uppercase : ") 
print(text.capitalize()) 

# original string never changes 
print("\nOriginal String") 
print(text)


# rstrip() Method
# Python String rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed). If no argument is passed, it removes trailing spaces.
a= "!!Harry!!!!!!"
print("rstrip Mathod")
print(a.rstrip("!"))


# replace() method
# Replaces all occurrences of a substring with another substring
print("replace Method")
print(a.replace("Harry","Jayesh"))


# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace
# string.split(separator, maxsplit)

name= "Jayesh Tejas Harry"
print("Split method")
print(name.split(" "))


# center() Method
# Python String center() Method tries to keep the new string length equal to the given length value and fills the extra characters using the default character (space in this case).
string = "geeks for geeks"
new_string = string.center(50)
# here fillchar not provided so takes space by default.
print(new_string)


# center() Method With ‘#’ as fillchar

string = "geeks for geeks"
new_string = string.center(24, '#')
# here fillchar is provided
print(new_string)

print("Length of string : ", len(string))
print("Length of new_string after fillchar : ", len(new_string))


# count() Method
# Python String count() function returns the number of occurrences of a substring within a String.

#initializing a string
my_string = "Banana"
#using string count() method
char_count = my_string.count('a')
#printing the result
print(char_count)
# It will give the number of times a occur in string



# endswith()
# Python String endswith() method returns True if a string ends with the given suffix, otherwise returns False.

# Syntax:  string.endswith(value, start, end)

# value:	Required, The value to check if the string ends with
# start	:Optional, An Integer specifying at which position to start the search

# end	:Optional, An Integer specifying at which position to end the search

txt = "Hello, welcome to my world."
print("Length :",len(txt))
x = txt.endswith("my world.", 5,27)
print(x)

text = "geeks for geeks."
# returns False
result = text.endswith('for geeks')
print (result)

# returns True
result = text.endswith('geeks.')
print (result)






# find() Method

# Python String find() method returns the lowest index or first occurrence of the substring if it is found in a given string.

# Syntax: string.find(value, start, end)
# start and end are optional values

# initializing a string
word = 'find me if you can'
# using string find() method
print(word.find('me'))
# return index 5



# isalnum() Method
# Python String isalnum() method checks whether all the characters in a given string are either alphabet or numeric (alphanumeric) characters.

# here a,b and c are characters and 1,2 and 3
# are numbers
string = "abc123"
print(string.isalnum())
# it will return True

# More examples
string = "abc 123"
print(string, "is alphanumeric?", string.isalnum())
#Return False

string = "abc_123"
print(string, "is alphanumeric?", string.isalnum())
#Return False

string = "000"
print(string, "is alphanumeric?", string.isalnum())
#Return True

string = "aaaa"
print(string, "is alphanumeric?", string.isalnum())
#Return True




# isalpha() Method
# Python String isalpha() method is used to check whether all characters in the String are an alphabet.

string = "geeks"
print(string.isalpha())
#Return True

# More Examples
# checking for alphabets
string = 'Ayush'
print(string.isalpha())
#Return True

string = 'Ayush0212'
print(string.isalpha())
#Return False

# checking if space is an alphabet
string = 'Ayush Saxena'
print( string.isalpha())
#Return False



# islower() Method
# Python String islower() method checks if all characters in the string are lowercase. 


print("geeks".islower())
#True

# initializing string 
islow_str = "geeksforgeeks"
not_islow = "Geeksforgeeks"

# checking which string is 
# completely lower 
print ("Is", islow_str, "full lower ? : " + str(islow_str.islower()))
#True

print ("Is", not_islow, "full lower ? : " + str(not_islow.islower()))
#False

