print("Tazo Kldiashvili") 
from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square
#drawing a door
forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
begin_fill()


penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(180,160)
pendown()
color("brown")
right(60)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
right(10)
begin_fill()
end_fill()
penup()
goto(20,160)





exitonclick()