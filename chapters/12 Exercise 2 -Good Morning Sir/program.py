import datetime

name = input("Enter your name\n")
current_time = datetime.datetime.now()
print("Current time is", current_time)
if current_time.hour<12:
    print('Good morning ',name)
elif current_time.hour<18:
    print('Good Afternoon ',name)
else:
    print('Good Evening',name)
    