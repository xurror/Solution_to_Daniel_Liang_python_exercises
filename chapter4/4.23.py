x, y = eval(input("Enter a point with two coordinates: "))

if (x > 10 / 2) or (y > 5 / 2):
    print("The point(" + str(x) + ", " + str(y) + ") is out of the rectangle")

elif (x <= 10 / 2) or (y <= 5 / 2):
    print("The point(" + str(x) + ", " + str(y) + ") is in the rectangle")
