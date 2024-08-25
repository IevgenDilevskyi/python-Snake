import time
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaaaake Game")
segments = []
screen.tracer(0)

for t in range(0,3):
    segment = Turtle("square")
    segment.pu()
    segment.color("white")
    segment.goto(x=-20 * t, y=0)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)














screen.exitonclick()