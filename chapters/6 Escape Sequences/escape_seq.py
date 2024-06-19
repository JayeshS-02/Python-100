# We want to print
# who's this?
'''If we execute this directly, we get an error message -'''

'''To overcome this problem, we can use escape sequences here'''
print('Who\'s this?')

'''n Escape Sequence in Python'''
print('Interview\nBit')


'''Backslash Escape Sequence in Python'''
print('Interview\\Bit')


'''Python Escape Sequence for Space'''
'''If we want to add tab space between words, then this escape sequence will give the tab space between the words or characters using “\t”.'''

# print('Interview\tBit')


'''Backspace Escape Sequence in Python'''
'''This escape sequence is used to remove the space between the words.'''

print('Interview \bBit')

'''Python escape sequence for Hexa value'''
'''Now, there may be a situation where we have Hexa values, and we want to print alphabets using their Hexa values? In such a case, we can use “\xhh”, where hh is the unique Hexa value of the alphabet.'''

print("\x48\x45\x4C\x4C\x4F\x20\x57\x4F\x52\x4C\x44")
# this will print (Hello World)


'''Python escape sequence for Octal value'''
'''Now, what if we want to print alphabets using their octal values? So for that, we will use “\ooo”, where ooo is the unique octal value of the alphabet.'''

print("\110\105\114\114\117\040\127\117\122\114\104")
# This will print (Hello World)