from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

hirst = Turtle()
hirst.penup()
hirst.goto(-190,-190)

# hirst.pendown()
# hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# hirst.dot(5)
# hirst.penup()
# left = hirst.xcor() +10
# hirst.goto(left, hirst.ycor())
# hirst.pendown()
# hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# hirst.dot(5)
# hirst.penup()
# left = hirst.xcor() +10
# hirst.goto(left, hirst.ycor())
# hirst.pendown()
# hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# hirst.dot(5)
# top = hirst.ycor() + 10
# hirst.goto(-190, top)
# hirst.pendown()
# hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# hirst.dot(5)
# hirst.penup()
# left = hirst.xcor() +10
# hirst.goto(left, hirst.ycor())
# hirst.pendown()
# hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# hirst.dot(5)
# hirst.penup()
# left = hirst.xcor() +10
# hirst.goto(left, hirst.ycor())
# hirst.pendown()
# hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
# hirst.dot(5)
top = -190
left = -190
hirst.speed(0)

while top < 200:
    while left < 200:
        hirst.pendown()
        hirst.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        hirst.dot(5)
        hirst.penup()
        left = hirst.xcor() +10
        hirst.goto(left, hirst.ycor())
    top = hirst.ycor() + 10
    left = -190
    hirst.goto(-190, top)


screen = Screen()
screen.exitonclick()
