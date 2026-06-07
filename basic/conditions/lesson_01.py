try:
    age = abs(int(input("What is your age? " )))
except ValueError:
    print("Please enter a valid age.")
    exit()
if(age<13):
    print("You are Child")
elif 13<=age<20:
    print("You are Teeneger")
elif 20<= age < 60:
    print("You are Adult")
else:
    print("You are Senior Citizan")