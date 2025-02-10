"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""

from random import *
from turtle import *

from freegames import vector

bird = vector(0, 0)
balls = []
score = 0
level = 1
ball_size = 20


def tap(x, y):
    """Move bird up in response to screen tap."""

    if score > 50:
        up = vector(0, 20)
    else:
        up = vector(0, 30)
    bird.move(up)


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    global score
    global level
    global ball_size
    """Draw screen objects."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, "green")
    else:
        dot(10, "red")

    for ball in balls:
        goto(ball.x, ball.y)
        if level >= 5:
            ball_size += 10
            dot(ball_size, "black")
        else:
            dot(ball_size, "black")

    score += 1
    if score % 100 == 0:
        level += 1
    goto(-190, 190)
    write(f"Score: {score}")
    goto(-190, 180)
    write(f"Level: {level}")
    update()


def move():
    global level
    global ball_size
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)
        if level == 1:
            pass
        elif level > 1 and level < 4:
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)
        else:
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < ball_size / 2:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)
    ontimer(bird, 500)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
