x, y = eval(input("Enter the center of the rectangle : "))
w, h = eval(input("Enter the width and height"))

import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(x, y)

turtle.goto(-(x + (w /2)), (y + (h /2)) )
turtle.pendown()
turtle.forward(w)
turtle.right(90)

turtle.forward(h)
turtle.right(90)

turtle.forward(w)
turtle.right(90)

turtle.forward(h)
turtle.right(90)
