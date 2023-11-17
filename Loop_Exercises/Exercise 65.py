import math
x1 = float(input("Enter the x part of the coordinate: "))
y1 = float(input("Enter the y part of the coordinate: "))
perimeter = 0
x2 = x1
y2 = y1
line = input("Enter the x part of the coordinate: (blank to quit): ")
while line != "":
    x3 = float(line)
    y3 = int(input("Enter the y part of the coordinate: "))
    distance = math.sqrt(((x2 - x3) * 2) + ((y2 - y3) * 2))
    perimeter = distance + perimeter
    x2 = x3
    y2 = y3
    line = input("Enter the x part of the coordinate: (blank to quit): ")
distance = math.sqrt(((x1 - x3) * 2 )+ ((y1 - y3) * 2))
perimeter = distance + perimeter
print("The perimeter of that polygon is", perimeter)