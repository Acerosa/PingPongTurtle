import  turtle as titi

# For the score
playerAScore = 0
playerBScore = 0

# creating the screen for the game
window = titi.Screen()
window.title('pinpong')
window.bgcolor('black')
window.setup(width=800, height=600)

# this is the right padle
rightPable = titi.Turtle()
rightPable.speed(0)
rightPable.shape('square')
rightPable.color('white')
rightPable.shapesize(stretch_wid=5, stretch_len=1)
rightPable.penup()
rightPable.goto(350, 0)


# this is the left padle
leftPable = titi.Turtle()
leftPable.speed(0)
leftPable.shape('square')
leftPable.color('white')
leftPable.shapesize(stretch_wid=5, stretch_len=1)
leftPable.penup()
leftPable.goto(-350, 0)

# This is the ball

ball = titi.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('orange')
ball.penup()
ball.goto(5,5)

# This will be to change the ball position on the screen
ballXDitction = 0.4
ballYDirection = 0.4

# This is the pen to write the score
pen = titi.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Ariel', 24, 'normal'))


# Functions to move the paddles up and down
def moveRightPadleUp():
    y = rightPable.ycor()
    y = y+90
    rightPable.sety(y)

def moveRightPadleDown():
    y = rightPable.ycor()
    y = y-90
    rightPable.sety(y)

def moveLeftPadleUp():
    y = leftPable.ycor()
    y = y+90
    rightPable.sety(y)

def moveLeftPadleDown():
    y = leftPable.ycor()
    y = y+90
    leftPable.sety(y)






