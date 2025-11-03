import turtle #Literally a turtle that we can command.
import time
import random
speed = 0.10

# This is for screen.
screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

#This is for snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('green')
snake.penup()
snake.goto(0, 100)
snake.direction = 'stop'

#This is for food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red') 
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

segment = []
score = 0

#This is for ScoreBoard and something like a length of the snake. 
penshad = turtle.Turtle()
penshad.speed(0)
penshad.shape('square')
penshad.color('white') 
penshad.penup()
penshad.goto(0, 260)
penshad.hideturtle()
penshad.write('Score: {}'. format(score), align='center', font=('Courier', 24, 'normal'))


#This is for game function.
#To set the movement directions. 
#ycor returns the current y-coordinate of the turtle's position
#xcor is self explanatory 
def movement():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

#This is for the movement to function. LOL?
def goUp():
    if snake.direction != 'down':
        snake.direction = 'up'

def goDown():
    if snake.direction != 'up':
        snake.direction = 'down'

def goRight():
    if snake.direction != 'left':
        snake.direction = 'right'

def goLeft():
    if snake.direction != 'right':
        snake.direction = 'left'

#For keyboard to work, you can change it to anything you want. 
screen.listen()
screen.onkey(goUp, 'Up')
screen.onkey(goDown, 'Down')
screen.onkey(goRight, 'Right')
screen.onkey(goLeft, 'Left')

#The whole game.
while True:
    screen.update()
    
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < - 300:
        time.sleep(1) #This is delay for each movement of the snake 
        snake.goto(0, 0)
        snake.direction = 'stop'

        for segment in segment:
            segment.goto(1000, 1000)

        segment = []
        score = 0
        penshad.clear()
        penshad.write('Score: {}'. format(score), align='center', font=('Courier', 24, 'normal'))

        speed = 0.15 

    if snake.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        score = score + 10
        penshad.clear()
        penshad.write('Score: {}'. format(score), align='center', font=('Courier', 24, 'normal'))

        #This line makes the snake go faster every time it eats food. 
        speed = speed -0.015

        #This is for a new start, if you lose, you'll start over, the speed will start to 0 as default.

        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape('square')
        newsegment.color('white')
        newsegment.penup()
        segment.append(newsegment)

    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)

    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x, y)

    movement()
    time.sleep(speed)
