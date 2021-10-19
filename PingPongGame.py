import turtle
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
rightPaddle = titi.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('white')
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)


# this is the left padle
leftPaddle = titi.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('white')
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# This is the ball

ball = titi.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('orange')
ball.penup()
ball.goto(5,5)

# This will be to change the ball position on the screen
ballXDirection = 0.4
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
    y = rightPaddle.ycor()
    y = y+90
    rightPaddle.sety(y)

def moveRightPadleDown():
    y = rightPaddle.ycor()
    y = y-90
    rightPaddle.sety(y)

def moveLeftPadleUp():
    y = leftPaddle.ycor()
    y = y+90
    leftPaddle.sety(y)

def moveLeftPadleDown():
    y = leftPaddle.ycor()
    y = y-90
    leftPaddle.sety(y)

window.listen()

window.onkey(moveLeftPadleUp, 'w')
window.onkey(moveLeftPadleDown,'s')
window.onkey(moveRightPadleUp, 'Up')
window.onkey(moveRightPadleDown, 'Down')



turtle.exitonclick()








