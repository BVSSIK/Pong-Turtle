# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# Part 1: Getting Started

import turtle
from turtle import *
import math
import winsound
wn = turtle.Screen()
wn.title('Pong by @BVSSIK')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)




#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)





#Ball
ball = turtle.Turtle()
ball.speed(-1)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
#ball.dx = 0
#ball.dy = 0
Vx = 0
Vy = 0
V = 0
A = 0


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'normal'))


#Starting Menu
menu = turtle.Turtle()
menu.speed(0)
menu.color('white')
menu.penup()
menu.hideturtle()
menu.goto(0, 100)
menu.write('Welcome to Pong\n', align='center', font=('Courier', 24, 'normal'))
menu.write('To start press "Spacebar"', align='center', font=('Courier', 24, 'normal'))
go = False







# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def play_wall_sound():
    winsound.PlaySound('wall.wav', winsound.SND_ASYNC)


def start():
    menu.clear()
    global go
    go = True




    




def move_ball():
    global V
    global A 
    global Vx
    global Vy
    # ball.setx(ball.xcor() + ball.dx)
    # ball.sety(ball.ycor() + ball.dy)
    #Calculating the velocity
    V = math.sqrt(Vx**2 + Vy**2)
    print("V: {}".format(V))
    print("Vx Before: {}".format(Vx))
    print("Vy Before: {}".format(Vy))

    #Calculating the angle
    # if Vx != 0:
    #     A = math.degrees(math.atan(Vy/Vx))
    #     if Vy<0 and Vx<0 or Vy>0 and Vx<0:
    #         A = A - 180
    #     elif Vy <0:
    #         A = 270
    #     else:
    #         A = 90
    #moving the turtle
    ball.seth(A)
    ball.fd(V/10000)

    #Changing the values of the velocities
    if Vx> 0:
        Vx-= 0.2
    elif Vx<0:
        Vx += 0.2
    

    if Vy < -2500:
        Vy+= 0.5
    else:
        Vy -= 0.5

    print("Vx After: {}".format(Vx))
    print("Vy After: {}".format(Vy))        







#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')
wn.onkeypress(start, 'space')
print(go)






#Main Game Loop
def runGame():
    # Score
    score_a = 0
    score_b = 0
    player_A = turtle.textinput("Player Name", "Player A:")
    player_B = turtle.textinput("Player Name", "Player B:")
    pen.write("{player_A}: {score_a}  {player_B}: {score_b}".format(player_A=player_A ,score_a=score_a, player_B=player_B, score_b=score_b), align='center', font=('Courier', 24, 'normal'))
    global go
    global Vx
    global Vy
    global A
    global V


    winsound.PlaySound("start_music.wav", winsound.SND_ASYNC | winsound.SND_NOSTOP)
    wn.listen()

    while True:
        wn.update()



        #Move the Ball
        # ball.setx(ball.xcor() + ball.dx)
        # ball.sety(ball.ycor() + ball.dy) 
        #print(go)

        if go:
            move_ball()
            


            #continue
        #Border Chekcing
        if ball.ycor() > 290:
            ball.sety(290)
            if A > 90 and A <= 270:
                transfer = 180 - A * 2
                A = 360 - abs(transfer)
            else:
                A = 360 - A



            play_wall_sound()

        if ball.ycor() < -290:
            ball.sety(-290)
            if A > 90 and A <= 270:
                transfer = 180 - A / 2
                A = 360 - abs(transfer)
            else:
                transfer = 180 - A * 2
                A += transfer
            play_wall_sound()

        #Scoring the Goal

        if ball.xcor() > 390:
            ball.goto(0, 0)
            score_a += 1
            A = 180
            pen.clear()
            pen.write("{player_A}: {score_a}  {player_B}: {score_b}".format(player_A=player_A ,score_a=score_a, player_B=player_B, score_b=score_b), align='center', font=('Courier', 24, 'normal'))
            go = False
            menu.write('{player_A} gets a Point\n'.format(player_A=player_A), align='center', font=('Courier', 24, 'normal'))
            menu.write('For next round press "Spacebar"', align='center', font=('Courier', 24, 'normal'))
            V = 0
            Vy = 0
            Vx = 0
        
        if ball.xcor() < -390:
            ball.goto(0, 0)
            score_b += 1
            A = 0
            pen.clear()
            pen.write("{player_A}: {score_a}  {player_B}: {score_b}".format(player_A=player_A ,score_a=score_a, player_B=player_B, score_b=score_b), align='center', font=('Courier', 24, 'normal'))
            go = False
            menu.write('{player_B} gets a Point\n'.format(player_B=player_B), align='center', font=('Courier', 24, 'normal'))
            menu.write('For next round press "Spacebar"', align='center', font=('Courier', 24, 'normal'))
            V = 0
            Vy = 0
            Vx = 0

        #Paddle Border Checking
        if paddle_a.ycor() > 300:
            paddle_a.sety(300)
        
        if paddle_a.ycor() < -300:
            paddle_a.sety(-300)

        if paddle_b.ycor() > 300:
            paddle_b.sety(300)
        
        if paddle_b.ycor() < -300:
            paddle_b.sety(-300)

        
        #Paddle and Ball Collisions
        if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 55) and (ball.ycor() > paddle_b.ycor() - 55):
            ball.setx(330)
            A = 180
            if ball.ycor() > paddle_b.ycor() + 20 and ball.ycor() < paddle_b.ycor() + 55:
                A -= 15
                if Vy > -7500:
                    Vy -= 2500
            elif ball.ycor() < paddle_b.ycor() -20 and ball.ycor() > paddle_b.ycor() - 55:
                A += 15
                if Vy > -7500:
                    Vy -= 2500
            winsound.PlaySound('paddleB.wav', winsound.SND_ASYNC)
        
        if ball.xcor() < -330 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 55) and (ball.ycor() > paddle_a.ycor() - 55):
            ball.setx(-330)
            A = 0
            if ball.ycor() > paddle_a.ycor() + 20 and ball.ycor() < paddle_a.ycor() + 55:
                A += 15
                if Vy > -7500:
                    Vy -= 2500
            elif ball.ycor() < paddle_a.ycor() -20 and ball.ycor() > paddle_a.ycor() - 55:
                A -= 15
                if Vy > -7500:
                    Vy -= 2500
            winsound.PlaySound('paddleA.wav', winsound.SND_ASYNC)


#Game Running
runGame()