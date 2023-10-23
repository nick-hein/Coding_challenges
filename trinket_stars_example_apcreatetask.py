#number of stars user input, list of different shades/colors of stars, function that makes star takes parameter star size. 

import turtle as trtl
import random

painter = trtl.Turtle()
painter.hideturtle()
painter.speed(0)

#draw background of night sky
trtl.bgcolor('black')

#ask user input for number and size of stars, , if statement if number of stars <1 or a decimal
size_of_stars = int(input('On a scale of 1 to 5, how big are the stars?'))
number_of_stars = (input('How many stars do you want to see?'))
for i in number_of_stars:
  if i == '.':
    number_of_stars = int(input('It must be an integer. How many stars do you want to see?'))
while int(number_of_stars) < 1:
  number_of_stars = (input('It must be an integer greater than or equal to 1. How many stars do you want to see?'))

#list of colors of stars
colors_of_stars = ['yellow','white','gold','gray','magenta']

#function that makes star with parameter of star size
def star(size_of_stars):
  star_color = random.choice(colors_of_stars)
  for i in range(8):
    painter.pencolor(star_color)
    painter.forward(size_of_stars)
    painter.backward(size_of_stars)
    painter.right(45)

#while loop to make number of stars
count = 0 
while count < int(number_of_stars):
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  star(size_of_stars)
  count += 1

wn = trtl.Screen()
wn.mainloop()