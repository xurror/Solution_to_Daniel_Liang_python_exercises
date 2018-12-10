
x1, y1 = eval(input("Enter the point p1 of a triangle: "))
x2, y2 = eval(input("Enter the point p2 of a triangle: "))
x3, y3 = eval(input("Enter the point p3 of a triangle: "))

import turtle
turtle.showturtle()

import math

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
#turtle.write("p1(", x1, y1, ")")

turtle.goto(x2, y2)
#turtle.write(x2, y2)

turtle.goto(x3, y3)
#turtle.write("p1(", x3, y3, ")")

turtle.goto(x1, y1)

d1 = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
d2 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
d3 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))

s = (d1 + d2 + d3) / 3

area = (s * ((s - d1) * (s - d2) * (s - d3))) ** (1 / 2)

turtle.penup()
turtle.goto(-25 + s, -60 + s)
turtle.pendown()

turtle.write("The area of the triangle is" + area)
