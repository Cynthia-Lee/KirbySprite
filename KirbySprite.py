from turtle import Turtle
myTurtle = Turtle()
myTurtle.hideturtle()
myTurtle.setpos(-200,200)
myTurtle.pos()
side = 20
#color pixel method
def square(color):
    myTurtle.color(color)
    myTurtle.begin_fill()
    for i in range(4):
        myTurtle.forward(side)
        myTurtle.right(90)
    myTurtle.end_fill()
    myTurtle.forward(side)
    
#next row method, doing rows from top to bottom
def nextRow(numSquares):
    myTurtle.penup()
    myTurtle.back(numSquares * side)
    myTurtle.right(90)
    myTurtle.forward(side)
    myTurtle.left(90)
    myTurtle.pendown()
    
# prints the row of pixels that color
def row(colors,numbers):
    numsquares = 0;
    for i in range(len(colors)):
        for i2 in range(numbers[i]):
            square(colors[i])
        numsquares += numbers[i]
    nextRow(numsquares) # reset the cursor
    
# colors we have
# colors = ["white" ,"black", "pink", "deeppink"]
pink = "#FF99CF"
darkpink = "#B54365"
# row 1
colors = ["white", "black", "white", "black", "white"]
numbers = [ 2, 2, 1, 5, 6]
row(colors,numbers)
# row 2
colors = ["white", "black", pink, "black", pink, "black", "white"]
numbers = [ 1, 1, 2, 1, 5, 2, 4]
row(colors,numbers)
# row 3 bppbppppppppbwww
colors = ["black", pink, "black", pink, "black", "white"]
numbers = [ 1, 2, 1, 8, 1, 3]
row(colors,numbers)
# row 4 bpppppbpbppppbww
for r in range(2): # row 4 and 5 are the same
    colors = ["black", pink, "black", pink, "black", pink, "black", "white"]
    numbers = [ 1, 5, 1, 1, 1, 4, 1, 2]
    row(colors,numbers)
# row 6 bpppppbpbpppppbw
colors = ["black", pink, "black", pink, "black", pink, "black", "white"]
numbers = [ 1, 5, 1, 1, 1, 5, 1, 1]
row(colors,numbers)
# row 7 bpppddpppddppppb
colors = ["black", pink, darkpink, pink, darkpink, pink, "black"]
numbers = [ 1, 3, 2, 3, 2, 4, 1]
row(colors,numbers)
# row 8 bppppppbpppppppb
colors = ["black", pink, "black", pink, "black"]
numbers = [ 1, 6, 1, 7, 1]
row(colors,numbers)
# row 9 wbpppppbpppppppb
colors = ["white", "black", pink, "black", pink, "black"]
numbers = [ 1, 1, 5, 1, 7, 1]
row(colors,numbers)
# row 10 wbppppppppppbbbw
colors = ["white", "black", pink, "black", "white"]
numbers = [ 1, 1, 10, 3, 1]
row(colors,numbers)
# row 11 wbpppppppppbdddb
colors = ["white", "black", pink, "black", darkpink, "black"]
numbers = [ 1, 1,9, 1, 3, 1]
row(colors,numbers)
# row 12 wwbpppppppbddddb
colors = ["white", "black", pink, "black", darkpink, "black"]
numbers = [ 2, 1, 7, 1, 4, 1]
row(colors,numbers)
# row 13  wwbbppppppbddddb
colors = ["white", "black", pink, "black", darkpink, "black"]
numbers = [ 2, 2, 6, 1, 4, 1]
row(colors,numbers)
# row 14 wbddbbpppbddddbw
colors = ["white", "black", darkpink, "black", pink, "black", darkpink, "black", "white"]
numbers = [ 1, 1, 2, 2, 3, 1, 4, 1, 1]
row(colors,numbers)
# row 15 bdddddbbbbbddbww
colors = ["black", darkpink, "black", darkpink, "black", "white"]
numbers = [ 1, 5, 5, 2, 1, 2]
row(colors,numbers)
# row 16 wbbbbbbwwwbbbwww
colors = ["white", "black", "white", "black", "white"]
numbers = [ 1, 6, 3, 3, 3]
row(colors,numbers)