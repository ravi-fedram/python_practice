import datetime 
age = int(input("What is your age? "))
day = datetime.datetime.now().strftime("%A")
price = 18 if age > 18 else 12
price = price -2 if day == "Sunday" else price
print(f"Your ticket price is: {price}") 
