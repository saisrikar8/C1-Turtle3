'''
03/29/2021
Review

Change color of pen
variable1.color(COLOR)
"yellow" / RGB / HEX
ex)
variable1.color("#008FFF")

Change size of pen(1 to 10)
variable1.width(WIDTH)
variable1.pensize(WIDTH)

Change turtle speed(1 to 10)
variable1.speed(SPEED)

#arrow
import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
pen.width(35)
pen.color("white")
pen.fd(100)
pen.right(135)
pen.fd(50)
pen.bk(50)
pen.left(135)
pen.left(135)
pen.fd(50)
'''


'''
1. Change shape of pen
variable1.shape(SHAPE)
SHAPE:arrow, turtle, circle, square, triangle, classic

ex)
pen.shape("circle")

2. Write text
variable1.write(TEXT)
variable1.write(TEXT, MOVE, ALIGN, FONT)

MOVE: True, False (Move the arrow along with the letters)
ALIGN: "left", "center", "right"
FONT: (FONTNAME, FONTSIZE, FONTSTYLE)

ex)
pen.write("Hello",False,"center", ("arial", 100, "bold"))

3. Fill color
variable1.begin_fill()
SQUARE
variable1.end_fill()

4. Clean the paper/background
variable1.clear()

5. Draw circle
variable1.circle(RADIUS)
variable1.circle(RADIUS, DEGREE)
variable1.circle(RADIUS, DEGREE, SIDE)


'''

import turtle


pen = turtle.Turtle()
'''
pen.pensize(5)
pen.color("green")
pen.penup()
pen.goto(-200,200)
pen.pendown()

pen.fillcolor("blue")
pen.begin_fill()
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.end_fill()

pen.home()
pen.circle(-100)
pen.width(1)
pen.color("red")
pen.circle(50, 180)
pen.left(90)
pen.fd(100)

pen.circle(1000, 360, 30)
'''

#HW: Draw a card

pen.clear()
pen.fd(100)
pen.left(90)
pen.fd(300)
pen.left(90)
pen.fd(200)
pen.left(90)
pen.fd(300)
pen.left(90)
pen.fd(100)
pen.penup()
pen.goto(-80, 10)
pen.pendown()
pen.write("A", False, "center", ("times new roman", 30, "normal"))
pen.penup()
pen.goto(60, 260)
pen.pendown()
pen.write("A", False, "center", ("times new roman", 30, "normal"))
pen.penup()
pen.goto(0,100)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.circle(60, 360, 4)
pen.end_fill()