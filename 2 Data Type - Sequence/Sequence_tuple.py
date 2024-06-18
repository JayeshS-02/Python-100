# Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by a tuple class. 

Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)
