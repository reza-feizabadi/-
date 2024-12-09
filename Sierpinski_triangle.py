import turtle
import random
def draw_sierpinski_with_dots(vertices, num_dots, colors):
    t = turtle.Turtle()
    t.hideturtle()  
    t.speed(0)  
    t.penup()  
    x, y = random.choice(vertices)
    for i in range(num_dots):
        t.goto(x, y)
        t.dot(3, colors[i % 3])  
        vx, vy = random.choice(vertices)
        x = (x + vx) / 2
        y = (y + vy) / 2
screen = turtle.Screen()
screen.bgcolor("white") 
vertices = [(-200, -150), (200, -150), (0, 200)]
colors = ["green", "blue", "red"] 
num_dots = 10000  
draw_sierpinski_with_dots(vertices, num_dots, colors)
turtle.done()
