"""
ITS 1801 F22 Exam 04
"""

import turtle

piper = turtle.Turtle()
casper = turtle.Turtle()
hazel = turtle.Turtle()

piper.shape("turtle")
casper.shape("triangle")
hazel.shape("classic")

piper.penup()
piper.goto(-150,0)
hazel.penup()
hazel.goto(150,0)
piper.pendown()
hazel.pendown()

# Do not modify anything above this line

def square(turtleName,lineColor):
  turtleName.color(lineColor)
  for i in range (4):
    turtleName.forward(50)
    turtleName.left(90)
    
    

def triangle(turtleName,lineColor):
  turtleName.color(lineColor)
  for i in range(3):
    turtleName.forward(50)
    turtleName.left(120)
    

def circle(turtleName,lineColor):
  turtleName.color(lineColor)
  turtleName.circle(50)


def draw(turtleName, shape, lineColor):
  if shape == '0':
    triangle(turtleName, lineColor)
    # Draw triangle using given turtleName and given lineColor and function triangle
  elif shape == '1':
    square(turtleName, lineColor)
    # Draw square using given turtleName and given lineColor and function square
  elif shape =='2':
    circle(turtleName, lineColor)
    # Draw circle using given turtleName and given lineColor and function circle
  else:
    print ('Wrong parameter selected and give to draw function')


print("This program has three turtles: Piper (left), Casper (middle) and Hazel (right)")
choiceTurtleStr = input("Select a turtle (0) Piper (1) Casper (2) Hazel: ")
choiceShapeStr = input ("Select a shape (0) triangle, (1) square, (2) circle: ")
choiceColorStr = input("Select a color (0) yellow, (1) blue, (2) red, (3) green: ")

# Define a list with your colors
colorList = ["yellow", "blue", "red", "green"]

# Transform the selected color in choiceColorStr into an integer
choiceColorInt = int(choiceColorStr)

if choiceTurtleStr == '0':
  draw(piper, choiceShapeStr, colorList[choiceColorInt])
  # Use the draw function to draw with piper the shape selected in choiceShapeStr and use choiceColorInt
  # as the index to select the corresponding color from colorList
elif choiceTurtleStr == '1':
  draw(casper, choiceShapeStr, colorList[choiceColorInt])
  # Use the draw function to draw with casper the shape selected in choiceShapeStr and use choiceColorInt
  # as the index to select the corresponding color from colorList
elif choiceTurtleStr == '2':
  draw(hazel, choiceShapeStr, colorList[choiceColorInt])
  # Use the draw function to draw with hazel the shape selected in choiceShapeStr and use choiceColorInt
  # as the index to select the corresponding color from colorList
else:
  print("Invalid turtle choice, not drawing anything")

# All items correct
