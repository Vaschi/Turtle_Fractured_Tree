import turtle
from inventory import draw_tree

# Screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fractal Tree")
# Turtle
t = turtle.Turtle()
t.speed(0)
#t.hideturtle()


t.penup()
t.left(90)
t.backward(100)
t.pendown()

draw_tree(100, t)
turtle.done()