import turtle
window = turtle.Screen()
myTurtle= turtle.Turtle()

window.bgcolor("lavender")
myTurtle.color("blue")
myTurtle.begin_fill()
myTurtle.forward(60)
myTurtle.left(120)
myTurtle.forward(60)
myTurtle.left(120)
myTurtle.forward(200)
myTurtle.end_fill()
myTurtle.color("red")
myTurtle.begin_fill()
myTurtle.left(120)
myTurtle.forward(200)
myTurtle.left(120)
myTurtle.forward(200)
myTurtle.end_fill()


# Move the turtle to an appropriate starting position
myTurtle.penup()
myTurtle.begin_fill()
myTurtle.color("yellow")
myTurtle.goto(-70, 0)  # Optional, change starting point
myTurtle.pendown()
myTurtle.left(180)  # Angle for an equilateral triangle
myTurtle.forward(200)
myTurtle.left(120)
myTurtle.forward(200)
myTurtle.left(120)
myTurtle.forward(200)

myTurtle.end_fill()
myTurtle.color("blue")
myTurtle.begin_fill()
myTurtle.teleport(27, -13)
myTurtle.circle(50)
myTurtle.end_fill()
myTurtle.color("green")
myTurtle.begin_fill()
myTurtle.circle(25)
myTurtle.teleport(27, -39)
myTurtle.end_fill()


myTurtle.hideturtle()
window.exitonclick()


