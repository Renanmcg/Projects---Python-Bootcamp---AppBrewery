#####Turtle Intro######

import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
'''timmy_the_turtle.forward(100)
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(180)
timmy_the_turtle.setheading(0)'''


######## Challenge 1 - Draw a Square ############
'''
for each in range(0, 4):
    timmy_the_turtle.forward(100)
    '''

######## Challenge 2 - Draw a Dashed Line ############

'''for _ in range(10):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()'''

######## Challenge 3 - Drawing Polygons ############
'''import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shapes(num_sides):

    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3, 16):
    timmy_the_turtle.color(random.choice(colours))
    draw_shapes(shape_side_n)'''

######## Challenge 4 - Random Walk ############

'''import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
directions = [0, 90, 180, 270]
for item in range(150):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))'''

######## Challenge 5 - Draw a Spirograph ############

import random
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



timmy_the_turtle.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


choice = float(input("What size of gap do you want?"))
draw_spirograph(choice)

screen = t.Screen()
screen.exitonclick()