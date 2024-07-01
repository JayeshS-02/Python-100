'''Python Lists'''

# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.

# marks=[3,5,6]
# print(marks)
# print("Type : ",type(marks)) #List
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[-1]) 


# marks = [3,5,6,"Harry",True]

# if 7 in marks:
#     print("Yes present")
# else:
#     print("Absent")



# marks = [3,5,6,"Harry",True]

# if "Harry" in marks:
#     print("Yes present")
# else:
#     print("Absent")


# same applies for sting as well
# if "ay" in "Jayesh":
#     print("yes")


# marks = [3,5,6,"Harry",True]
# print(marks[2:4]) #2 and 3 included except 4



# lst = [i*i for i in range(4)]
# print(lst)

lst = [i*i for i in range(20) if i%2==0]
print(lst)