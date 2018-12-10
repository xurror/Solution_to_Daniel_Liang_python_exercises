import turtle
turtle.showturtle()
#head
turtle.circle(100)
#nose
turtle.penup()
turtle.goto(0, 110)
turtle.pendown()

turtle.right(72)
turtle.forward(50)

turtle.penup()
turtle.goto(0, 110)
turtle.pendown()

turtle.right(36)
turtle.forward(50)
#mouth
turtle.penup()
turtle.forward(10)
turtle.pendown()

turtle.penup()
turtle.right(72)
turtle.forward(5)
turtle.pendown()


turtle.penup()
turtle.right(-170)
turtle.forward(5)
turtle.pendown()
turtle.forward(20)

turtle.right(-20)
turtle.forward(20)
#eyes
turtle.penup()
turtle.goto(30, 125)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-30, 125)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
