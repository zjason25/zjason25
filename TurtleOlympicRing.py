import turtle

s = turtle.Screen()
t = turtle.Turtle()


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def olympic(t):
    t.circle(30)

    jump(t,-70, 0)
    t.circle(30)

    jump(t, 70, 0)
    t.circle(30)

    jump(t, -35, -30)
    t.circle(30)

    jump(t, 35, -30)
    t.circle(30)

olympic(t)
