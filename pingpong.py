import turtle

wn = turtle.Screen()
wn.title("Pong by @Ali")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# Score
score_a = 0
score_b = 0

# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)


# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 7
ball.dy = -7

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0  Player B : 0", align="center", font=("Courier", 24, "normal"))


#function
def paddle1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "i")
wn.onkeypress(paddle2_down, "k")

while True:   #main game
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390) #ball.got0(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390) #ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #collision
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
