x, y = eval(input("Enter the x and y coordinates of the center of the circle : "))
r = eval(input("Enter the radius of the circle : "))

PI = 3.1428571429
A = PI * r *r

import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.circle(r)
turtle.penup()
turtle.goto(x, (y + r))
turtle.pendown()
turtle.write(A)

