import math

marks : int = 10
first_name = "Suryaansh"

print(marks)
print(first_name)   

total_marks = marks
print(total_marks)

marks = 20

print(marks)
print(total_marks)

print("#####  List ####")
my_subjects = ["Maths", "Science", "English"]

print(my_subjects)
my_subjects.append("History")
print(my_subjects)
my_subjects[0] = "Physics"
my_subjects.append("Maths")
print(my_subjects)

print(my_subjects[1:3])

#print(dir(my_subjects))
print(len(my_subjects))
print(my_subjects)
my_subjects.pop(3)
print("My subjects after popping index 3:", my_subjects)
my_subjects.insert(2, "biology")
print("My subjects after inserting 'biology' at index 2:", my_subjects)

print("#####  tuple ####")
my_directions = ("North", "South", "East", "West","North")
print(my_directions)
##print(dir(my_directions))
print(my_directions.count("North"))
print(len(my_directions))


print("#####  Dictionary ####")
my_marks = {"Maths": 95, "Science": 90, "English": 85}
print(my_marks)
my_marks["History"] = 80
print(my_marks)

print(dir(my_marks))