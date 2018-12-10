x0, y0, x1, y1, x2, y2 = eval(input("Enter the x and Y coordinates of the points p0, p1 and p2 respectively: "))

a = (x1 - x0) * (y2 - y0)
b = (x2 - x0) * (y1 - y0)

if (a - b) == 0:
    print("("
          + str(format(x2, ".1f"))
          + ","
          + str(format(y2, ".1f"))
          + ")is on the same line segment from ("
          + str(format(x0, ".1f"))
          + ","
          + str(format(y0, ".1f"))
          + ") to ("
          + str(format(x1, ".1f"))
          + ","
          + str(format(y1, ".1f"))
          +")")
else:
    print("("
          + str(format(x2, ".1f"))
          + ","
          + str(format(y2, ".1f"))
          + ")is not on the same line segment from ("
          + str(format(x0, ".1f"))
          + ","
          + str(format(y0, ".1f"))
          + ") to ("
          + str(format(x1, ".1f"))
          + ","
          + str(format(y1, ".1f"))
          + ")")
