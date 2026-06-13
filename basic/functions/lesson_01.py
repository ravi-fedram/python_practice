import math
def circle_area_circumference(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_area_circumference(3)
print("Area of circle = ",round(a,2), " Circumference of circle = ",round(c,2))
