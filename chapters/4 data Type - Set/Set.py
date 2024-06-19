# In Python Data Types, a Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.

set1 = set()
print("Initial blank Set: ")
print(set1)

set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

# Accessing Set Items
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
print("Geeks" in set1)

