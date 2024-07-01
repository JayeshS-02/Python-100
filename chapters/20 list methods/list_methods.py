# 1.  append() method
# The append() method appends an element to the end of the list.

# list=[2,3,4,5]
# print("printing before append: " ,list)
# print("\nAppending")
# list.append(10)
# print("printing after append: " ,list)


# # using list fruits 
# fruits = ["apple", "cherry", "banana"] 

# # adding new element grapes 
# fruits.append("grapes") 

# # priting the fruits list 
# print(fruits) 


# # my_list 
# my_list = ['geeks', 'for', 'geeks'] 
# # another list 
# another_list = [6, 0, 4, 1] 
# # append another_list to my_list 
# my_list.append(another_list) 
# print(my_list)


# 2. extend() Method
'''The extend() method adds all the items of the specified iterable, such as list, tuple, dictionary, or string , to the end of a list.'''
numbers1 = [3, 4, 5]
numbers2 = [10, 20]
# add the items of numbers1 to the number2 list
numbers2.extend(numbers1)
print(f"numbers1 = {numbers1}")
print(f"numbers2 = {numbers2}")



# 3. sort() method
# alphabets = ['a','e','d','c','b'] 
# alphabets.sort() 
# print(alphabets) 


#Sorting in Ascending order
# random_numbers = [2,5,6,1,8,3] 
# random_numbers.sort() 
# print(random_numbers)


#Sorting in Descending order
# random_numbers = [2,5,6,1,8,3] 
# random_numbers.sort(reverse=True) 
# print(random_numbers)


#4. reverse() method
# fruits = ['apple', 'cherry', 'banana']
# fruits.reverse()
# print(fruits)

# string = "Jayesh"
# string.reverse()
# print(string)
'''This will give error if string is used in place of list'''


# reverse using slicing method
# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)



'''reversing a sublist using Slicing'''
# my_list = [1, 2, 3, 4, 5]
# print('Original list:', my_list)
# my_list[1:4] = my_list[1:4][::-1]
# print('Reversed sublist:', my_list)

'''accessing elements in reversed order'''
# my_list = [1, 2, 3, 4, 5]
# for element in reversed(my_list):
# 	print(element)


#5 index() method
'''List index() method searches for a given element from the start of the list and returns the position of the first occurrence.'''
# Syntax
# list_name.index(element, start, end) 

# animal = [ "dog", "cat","bear","lion","tiger"]
# print(animal.index("tiger"))


# list of items 
# list1 = ["dog","tiger","lion","dog","cat", "cat","bear","lion","tiger"] 

# # Will print index of '4' in sublist 
# # having index from 4 to 8. 
# print(list1.index("cat", 4, 8)) 



# # list of items 
# list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 

# # Will print index of '4' in sublist 
# # having index from 4 to 8. 
# print(list1.index(4, 4, 8))



# 6 count() Method
# list1=["dog","cat","tiger","lion","cat","cat","dog","lion"]
# print("Count of cat in list : ", list1.count("cat"))


# 7 copy() method
# l = [1,2,3,4,5]
# m=l.copy()
# print(m)
# m[0]=100
# print(m)
# print(l)
#original did not changed after creating copy


# 8 insert() method
'''Python List insert() method inserts an item at a specific index in a list.'''

# # creating a list 
# fruit = ["banana","cherry","grape"] 
# fruit.insert(1,"apple") 
# print(fruit)


# list = ['Sun', 'rises', 'in', 'the', 'east'] 
# list.insert(0, "The") 
# print(list)


'''Inserting a tuple into the List'''
# list1 = [ 1, 2, 3, 4, 5, 6 ] 

# # tuple of numbers 
# num_tuple = (4, 5, 6) 

# # inserting a tuple to the list 
# list1.insert(2, num_tuple) 

# print(list1)


'''Insert List in another List'''
# list1 = [1, 2, 3] 
# list2 = [4, 5, 6] 

# list1=list1+list2 

# print(list1) 







