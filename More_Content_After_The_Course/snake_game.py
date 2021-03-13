import os
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#set up screen
window1 = turtle.Screen()
window1.title("Snake Game")
window1.bgcolor('black')
window1.setup(width=600, height=600)
window1.tracer(0)

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("yellow")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.write("Score: 0  High Score: 0", align = "center", font=("ds-digital", 24, "normal"))

#Functions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"
def go_down():
    if snake.direction != "up":
        snake.direction = "down"
def go_left():
    if snake.direction != "right":
        snake.direction = "left"
def go_right():
    if snake.direction != "left":
        snake.direction = "right"
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

#keyboard
window1.listen()
window1.onkeypress(go_up, "w")
window1.onkeypress(go_down, "s")
window1.onkeypress(go_left, "a")
window1.onkeypress(go_right, "d")

#MainLoop
while True:
    window1.update()

    #check collision with border area
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()

        #reset
        score = 0
        delay = 0.1

        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    #check if got food
    if snake.distance(food) <20:
        # move the food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(snake)<20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #update the score     
            scoreboard.clear()
            scoreboard.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
window1.mainloop()