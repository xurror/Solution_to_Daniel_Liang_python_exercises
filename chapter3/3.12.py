l = eval(input("Enter the length of the star: "))

import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

turtle.right(72)
turtle.forward(l)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

turtle.right(36)
turtle.forward(l)

turtle.right(-144)
turtle.forward(l)

turtle.right(-144)
turtle.forward(l)

turtle.right(-144)
turtle.forward(l)
