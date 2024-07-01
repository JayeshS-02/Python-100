numbers = [1, 2, 3, 4, 5] 
squared = [x ** 2 for x in numbers] 
print(squared)


# Using list comprehension to iterate through loop 
List = [character for character in [1, 2, 3]] 

# Displaying list 
print(List)



'''Even List'''
list = [i for i in range(11) if i % 2 == 0] 
print(list)



'''Matrix'''
matrix = [[j for j in range(3)] for i in range(3)] 
	
print(matrix)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

