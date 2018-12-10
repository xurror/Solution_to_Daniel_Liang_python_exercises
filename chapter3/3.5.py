import math

n = eval(input("Enter the number side: "))
s = eval(input("Enter the side: "))

area = (n * math.pow(s, 2)) / (4 * math.tan(math.pi / n))
print("The area of the polygon is", area)