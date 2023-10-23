
#create a house that asks for user input for color of house itself, garage, front door, and roof. 
#also asks for sunny/rainy day which will create either flowers (procedure) or puddles(procedure)
#if sunny, ask for flower colors. If rainy, ask for how much rain(determine size of puddle)

import turtle as trtl 

#user inputs for house, sunny/rainy day
house_color = input('What color do you want your house to be?')
roof_color = input('What color do you want your roof to be?')
garage_color = input('What color do you want your garage to be?')
door_color = input('What color do you want your front door to be?')
daily_weather = input('Is it a sunny or rainy day?')

#keep track of user inputs in a list
user_inputs = []
user_inputs.append(house_color)
user_inputs.append(roof_color)
user_inputs.append(garage_color)
user_inputs.append(door_color)
user_inputs.append(daily_weather)

#create pencil
pencil = trtl.Turtle()

#create house
#house
pencil.fillcolor(user_inputs[0])
pencil.begin_fill()
pencil.goto(-50,-50)
pencil.goto(-50,0)
pencil.goto(0,50)
pencil.goto(0,0)
pencil.goto(50,-50)
pencil.goto(50,0)
pencil.goto(0,50)
pencil.end_fill()
#roof
pencil.fillcolor(user_inputs[1])
pencil.begin_fill()
pencil.goto(0,80)
pencil.goto(-50,30)
pencil.goto(-50,0)
pencil.goto(0,50)
pencil.goto(50,0)
pencil.goto(50,30)
pencil.goto(0,80)
pencil.end_fill()
#yard
pencil.penup()
pencil.fillcolor('light green')
pencil.begin_fill()
pencil.goto(50,30)
pencil.pendown()
pencil.goto(50,-50)
pencil.goto(120,-50)
pencil.goto(120,30)
pencil.goto(50,30)
pencil.end_fill()
#garage
pencil.penup()
pencil.goto(10,-10)
pencil.fillcolor(user_inputs[2])
pencil.begin_fill()
pencil.pendown()
pencil.goto(10,20)
pencil.goto(40,-10)
pencil.goto(40,-40)
pencil.end_fill()
#door
pencil.penup()
pencil.fillcolor(user_inputs[3])
pencil.begin_fill()
pencil.goto(-10,-10)
pencil.pendown()
pencil.goto(-10,10)
pencil.goto(-20,0)
pencil.goto(-20,-20)
pencil.goto(-10,-10)
pencil.end_fill()


#procedure for sunny/rainy day
def sunny_day(flower_color):
  typical_flower_colors = ['red','blue','yellow','orange','purple', 'green']
  while flower_color not in typical_flower_colors:
    flower_color = input('That is not a flower color in your yard. Pick a different color?')

  #make flowers
  y = 20
  while y > -40:
    x = 60
    y = y -10
    pencil.penup()
    pencil.goto(x,y)
    pencil.pendown()
    pencil.setheading(90)
    pencil.forward(5)
    pencil.fillcolor(flower_color)
    pencil.begin_fill()
    pencil.circle(2)
    pencil.end_fill()
    while x <= 90:
      x = x + 10
      pencil.penup()
      pencil.goto(x,y)
      pencil.pendown()
      pencil.pencolor('brown')
      pencil.setheading(90)
      pencil.forward(5)
      pencil.fillcolor(flower_color)
      pencil.begin_fill()
      pencil.circle(2)
      pencil.end_fill()

if daily_weather == 'sunny':
  flower_color = input('You have flowers that are blooming! What color are they?')
  sunny_day(flower_color)
if daily_weather == 'rainy':
  print('A rainy day means puddles in your yard')
  #make 2 puddles in yard
  y = 10
  while y >= -40:
    pencil.penup()
    pencil.goto(85,y)
    pencil.pendown()
    pencil.fillcolor('light blue')
    pencil.begin_fill()
    pencil.circle(7)
    pencil.end_fill()
    y = y - 20

print('\nYou have a great looking house!')
print(user_inputs)

wn = trtl.Screen()
wn.mainloop()