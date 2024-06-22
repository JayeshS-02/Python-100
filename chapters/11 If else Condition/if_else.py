# If - else statement
# age = int(input("Enter your age\n"))
# print("Your age is: ",age)
# if age>=18:
#     print("You can drive")
# else:
#     print("You cannot drive")


# If-else-elif Statement
# num = int(input("Enter the value of num\n"))
# if(num<0):
#     print("Num is negative")
# elif(num==0):
#     print("Num is equal to 0")
# else:
#     print("Num is greater than 0")


# Nested If else Statements
num = int(input("Enter the value of num\n"))
if(num==0):
    print("Number is equal to 0")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is less than 0")