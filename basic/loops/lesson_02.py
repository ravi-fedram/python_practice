
num = 0
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if num in range(1, 11):
        break

