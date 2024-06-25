# day = input("Enter day of week\n")
# match day:
#     case "Monday":
#         print("Its Monday")
#     case "Tuesday":
#         print("Its Tuesday")
#     case "Wed":
#         print("Its Tuesday")
#     case "Thu":
#         print("Its Tuesday")
#     case _:
#         print("Invalid day")


# num = int(input("Enter a number\n"))
# match num:
#     case 1:
#         print("Entered 1")
#     case 2:
#         print("Entered 2")
#     case 3:
#         print("Entered 3")
#     case _:
#         print("Entered number except 1,2,3")


# num = int(input("Enter a number between 1 and 6: "))
    
#     # match case
# match num:
#     # pattern 1
#     case 1 | 2:
#         print("One or Two")
#     # pattern 2
#     case 3 | 4:
#         print("Three or Four")
#     # pattern 3
#     case 5 | 6:
#         print("Five or Six")
#     # default pattern
#     case _:
#         print("Number not between 1 and 6")




# Match Case Statement with Python If Condition
num = int(input("Enter a number: "))
    
    # match case
match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")
            