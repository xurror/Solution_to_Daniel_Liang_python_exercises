x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinate, width, and height: "))
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinate, width, and height: "))

x = w1 - w2
x = abs(x)
y = h1 - h2
y = abs(y)

a1 = (w1 / 2) + abs(x1)
a2 = (w2 / 2) + abs(x2)
b1 = (h1 / 2) + abs(y1)
b2 = (h2 / 2) + abs(y2)

area1 = w1 * h1
area2 = w2 * h2

if (x1 and x2) >= 0:
    if abs(area1) > abs(area2):
        if (abs(a1) > abs(a2)) and (abs(b1) > abs(b2)):
            print("r2 is inside r1")

elif area1 < area2:
    if abs(x2 - w2) > w1:
        if abs(y2 - h2) > h1:
            print("r1 is inside r2")
    elif abs(x2 - w2) < w1:
        if abs(y2 - h2) > h1:
            print("r1 overlaps on r2")
    elif abs(x2 - w2) > w1:
        if abs(y2 - h2) < h1:
            print("r1 overlaps on r2")
    elif abs(x2 - w2) < w1:
        if abs(y2 - h2) > h1:
            print("r1 overlaps on r2")
