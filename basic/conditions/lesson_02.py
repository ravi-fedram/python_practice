from datetime import date
coupon_applied = False
try:
    age = abs(int(input("What is your age? " )))
except ValueError:
    print("Please enter a valid age.")
    exit()
price = 12 if age >= 18 else 8
if date.today().strftime("%A") == "Monday":
    price -= 2
    coupon_applied = True
print("Ticket priec for you is ",price, "Monday Coupon applied" if coupon_applied else "")