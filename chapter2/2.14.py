x1, y1, x2, y2, x3, y3 = eval(input("Enter three points of a triangle : "))

print(x1, y1)
print(x2, y2)
print(x3, y3)

side1 = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
side2 = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** (1 / 2)
side3 = (((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** (1 / 2)

s = (side1 + side2 + side3) / 2

area = (s * ((s - side1) * (s - side2) * (s - side3))) ** (1 / 2)

print("The area of the triangle is", area)
