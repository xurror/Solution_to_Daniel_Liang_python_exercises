import math
x, y = eval(input("Enter a point with two coordinates: "))

d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

if d > 10:
    print("The point(" + str(format(x, "0.1f")) + ", " + str(format(y, "0.1f")) + ") is out of the circle")

elif d <= 10:
    print("The point(" + str(format(x, "0.1f")) + ", " + str(format(y, "0.1f")) + ") is in the circle")
