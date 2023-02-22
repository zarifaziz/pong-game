import turtle

# create the game window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)

# paddle size
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

# ball size
BALL_SIZE = 10

# set initial score
left_score = 0
right_score = 0

# create paddles
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=PADDLE_HEIGHT/20, stretch_len=PADDLE_WIDTH/20)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=PADDLE_HEIGHT/20, stretch_len=PADDLE_WIDTH/20)
right_paddle.penup()
right_paddle.goto(350, 0)

# create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(BALL_SIZE/20, BALL_SIZE/20)
ball.penup()
ball.goto(0, 0)
ball_speed_x = 5
ball_speed_y = 5

# create scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

# move the paddles
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# handle user input
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# game loop
while True:
    # move the ball
    ball.setx(ball.xcor() + ball_speed_x)
    ball.sety(ball.ycor() + ball_speed_y)

    # check for collisions with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball_speed_y = -ball_speed_y

    # check for collisions with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball_speed_x = -ball_speed_x

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball_speed_x = -ball_speed_x

    # check for scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_speed_x = -ball_speed_x
        left_score += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_speed_x = -ball_speed_x
        right_score += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    # update the window
    window.update()


