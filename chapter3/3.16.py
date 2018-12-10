import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

turtle.begin_fill()
turtle.circle(25, steps = 3)
turtle.end_fill()

turtle.penup()
turtle.goto(-120, 0)
turtle.pendown()
turtle.color("gray")
turtle.begin_fill()
turtle.circle(25, steps = 4)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, 0)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(25, steps = 5)
turtle.end_fill()

turtle.penup()
turtle.goto(40, 0)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(25, steps = 6)
turtle.end_fill()

turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.color("purple")
turtle.begin_fill()
turtle.circle(25, steps = 7)
turtle.end_fill()

