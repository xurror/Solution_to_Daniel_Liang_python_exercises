
import turtle
turtle.showturtle()

turtle.begin_fill()
turtle.circle(100, steps = 6)
turtle.end_fill()

turtle.goto(-75, 75)
turtle.color("white")
turtle.write("STOP", font = ("Seriff", 40, "bold"))

turtle.color("black")
