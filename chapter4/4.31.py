x0, y0, x1, y1, x2, y2 = eval(input("Enter the x and Y coordinates of the points p0, p1 and p2 respectively: "))

a = (x1 - x0) * (y2 - y0)
b = (x2 - x0) * (y1 - y0)

if (a - b) > 0:
    print("p2 is on the left side of the line")
elif (a - b) < 0:
    print("p2 is on the right side of the line")
elif (a - b) == 0:
    print("p2 is on thesame line from p0 to p1")
