# String Slicing

# In Python Programming tutorials, the String Slicing method is used to access a range of characters in the String. Slicing in a String is done by using a Slicing operator, i.e., a colon (:).  One thing to keep in mind while using this method is that the string returned after slicing includes the character at the start index but not the character at the last index.

# Creating a String
String1 = "JayeshGeeks"
print("Initial String: ")
print(String1)


print("Length of string is : ",len(String1))

# Printing 3rd to 12th character
print("\nSlicing characters from 1-10: where index 1 is included ans index 10 in not included")
print(String1[1:10])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print("Here 5th index is included and -2 index is not includud")
print(String1[5:-2])



# String Reversed


string = "Jayesh"
print("reversing the string using string slicing method")
print(string[::-1])
