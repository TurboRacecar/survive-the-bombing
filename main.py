import turtle
import time
import random
import winsound

turtle.register_shape("dodger.png")
turtle.register_shape("ground.png")
turtle.register_shape("projectile.png")


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=600, width=1000)
wn.tracer(0)
wn.title("Dodger game by @TurboRacecar")

player = turtle.Turtle()
player.color("cyan")
player.speed(0)
player.shape("dodger.png")
player.penup()
player.goto(0, -260)

sfx = True

projectile = turtle.Turtle()
projectile.color("cyan")
projectile.speed(0)
projectile.shape("projectile.png")
projectile.penup()
projectile.goto(0, 380)

prodspeed = 16

mode = "playing"

projectile1 = turtle.Turtle()
projectile1.color("cyan")
projectile1.speed(0)
projectile1.shape("projectile.png")
projectile1.penup()
projectile1.goto(60, 500)

projectile2 = turtle.Turtle()
projectile2.color("cyan")
projectile2.speed(0)
projectile2.shape("projectile.png")
projectile2.penup()
projectile2.goto(-60, 620)

projectile3 = turtle.Turtle()
projectile3.color("cyan")
projectile3.speed(0)
projectile3.shape("projectile.png")
projectile3.penup()
projectile3.goto(120, 740)

projectile4 = turtle.Turtle()
projectile4.color("cyan")
projectile4.speed(0)
projectile4.shape("projectile.png")
projectile4.penup()
projectile4.goto(-120, 864)

ground = turtle.Turtle()
ground.color("lime")
ground.speed(0)
ground.shape("ground.png")
ground.penup()
ground.goto(0, -280)
ground.shapesize(stretch_len=50, stretch_wid=1)

pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(496, 300)
pen.pendown()
pen.pensize(8)
pen.goto(496, -300)
pen.goto(-500, -300)
pen.goto(-500, 300)
pen.goto(496, 300)
pen.penup()
del(pen)

pen2 = turtle.Turtle()
pen2.color("gold")
pen2.hideturtle()
pen2.pensize(5)

pen1 = turtle.Turtle()
pen1.penup()
pen1.goto(0, 100)
pen1.color("white")
pen1.hideturtle()
pen1.pensize(8)


def respawn():
    global mode
    wn.bgcolor("black")
    mode = True
    pen1.clear()
    pen2.clear()
    player.showturtle()
    projectile.showturtle()
    projectile1.showturtle()
    projectile2.showturtle()
    projectile3.showturtle()
    projectile4.showturtle()


def game_over():
    global mode
    pen1.write("Game Over", align="center", font=("Courier", 20, "normal"))
    pen2.write("press r to restart", align="center", font=("Courier", 20, "normal"))
    wn.bgcolor("red")
    wn.onkeypress(respawn, "r")
    projectile.hideturtle()
    projectile1.hideturtle()
    projectile2.hideturtle()
    projectile3.hideturtle()
    projectile4.hideturtle()
    mode = False


def right():
    global mode
    if mode:
        x = player.xcor()
        x += 20
        player.setx(x)


def left():
    global mode
    if mode:
        x = player.xcor()
        x -= 20
        player.setx(x)


def projectile_go_down():
    y = projectile.ycor()
    y -= prodspeed
    projectile.sety(y)

    y = projectile1.ycor()
    y -= prodspeed
    projectile1.sety(y)

    y = projectile2.ycor()
    y -= prodspeed
    projectile2.sety(y)

    y = projectile3.ycor()
    y -= prodspeed
    projectile3.sety(y)

    y = projectile4.ycor()
    y -= prodspeed
    projectile4.sety(y)


def pause():
    global mode
    if mode:
        wn.bgcolor("black")
        mode = True
        pen1.clear()
        pen2.clear()
        player.showturtle()
        mode = False

    elif not mode:
        mode = True
        wn.bgcolor("black")
        mode = True
        pen1.clear()
        pen2.clear()
        player.showturtle()


def sound():
    global sfx
    if sfx:
        sfx = False
    elif not sfx:
        sfx = True


wn.listen()
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(pause, "Escape")
wn.onkeypress(sound, "s")

while True:
    if mode:
        if prodspeed > 24:
            prodspeed = 24
        wn.update()
        projectile_go_down()
        time.sleep(0.04)

        if player.xcor() < -480:
            player.setx(-480)

        if player.xcor() > 480:
            player.setx(480)

        if projectile.ycor() < -260:
            wn.setup(height=600, width=1000)
            projectile.sety(280)
            x = random.randint(-480, 480)
            projectile.setx(x)
            if sfx:
                winsound.PlaySound("audio_explosion.wav", 1)
            prodspeed += 0.1

        if projectile1.ycor() < -260:
            wn.setup(height=600, width=1000)
            projectile1.sety(280)
            x = random.randint(-480, 480)
            projectile1.setx(x)
            if sfx:
                winsound.PlaySound("audio_explosion.wav", 1)
            prodspeed += 0.1

        if projectile2.ycor() < -260:
            wn.setup(height=600, width=1000)
            projectile2.sety(280)
            x = random.randint(-480, 480)
            projectile2.setx(x)
            if sfx:
                winsound.PlaySound("audio_explosion.wav", 1)
            prodspeed += 0.1

        if projectile3.ycor() < -260:
            wn.setup(height=600, width=1000)
            projectile3.sety(280)
            x = random.randint(-480, 480)
            projectile3.setx(x)
            if sfx:
                winsound.PlaySound("audio_explosion.wav", 1)
            prodspeed += 0.1

        if projectile4.ycor() < -260:
            wn.setup(height=600, width=1000)
            projectile4.sety(280)
            x = random.randint(-480, 480)
            projectile4.setx(x)
            if sfx:
                winsound.PlaySound("audio_explosion.wav", 1)
            prodspeed += 0.1

        if player.distance(projectile) < 30:
            player.hideturtle()
            projectile.sety(280)
            x = random.randint(-480, 480)
            projectile.setx(x)
            winsound.PlaySound("oof.wav", 1)
            game_over()

        if player.distance(projectile1) < 30:
            player.hideturtle()
            projectile1.sety(280)
            x = random.randint(-480, 480)
            projectile1.setx(x)
            winsound.PlaySound("oof.wav", 1)
            game_over()

        if player.distance(projectile2) < 30:
            player.hideturtle()
            projectile2.sety(280)
            x = random.randint(-480, 480)
            projectile2.setx(x)
            winsound.PlaySound("oof.wav", 1)
            game_over()

        if player.distance(projectile3) < 30:
            player.hideturtle()
            projectile3.sety(280)
            x = random.randint(-480, 480)
            projectile3.setx(x)
            winsound.PlaySound("oof.wav", 1)
            game_over()

        if player.distance(projectile4) < 30:
            player.hideturtle()
            projectile4.sety(280)
            x = random.randint(-480, 480)
            projectile4.setx(x)
            winsound.PlaySound("oof.wav", 1)
            game_over()
        print(prodspeed)
    else:
        wn.update()
        if player.xcor() < -480:
            player.setx(-480)

        if player.xcor() > 480:
            player.setx(480)
