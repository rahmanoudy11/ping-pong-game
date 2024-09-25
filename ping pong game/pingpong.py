import turtle
#setup window=============opject assgiment as window 
window = turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=800,height=600)
#when update the image not delay on the time (set delay for update drwings)
window.tracer(0)   
window.bgcolor(.1, .1, .1)


#setup game objects=========
#ball
ball=turtle.Turtle()
#darwing speed fastest (1---->10) 0=10 اسرع ما يمكن 
ball.speed(0)
ball.shape("square")  #لو عملتها مربع الحجم بتاعها افتراضي بيحطه 20و20علشان اغير لازم شابسيز بstretch
ball.color("white")
ball.shapesize(stretch_len=1, stretch_wid=1)  #بياخد الرقم ويضربه في 20
ball.goto(x=0 ,y=0) #اخلي الكوره في النص بامر جوتو
ball.penup() # كانه بيرسم خطوط هنا لما اعملها مش هيرسم 
ball_dx=1
ball_dy=1
ball_speed=.5


#center line =================
centerLine=turtle.Turtle()
centerLine.speed(0)
centerLine.shape("square")
centerLine.color("white")
centerLine.shapesize(stretch_len=.1, stretch_wid=25)
centerLine.goto(x=0, y=0)
centerLine.penup()

# player1=================
player1 =turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.goto(x=-350, y=0)
player1.penup()


# player2=================
player2 =turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.goto(x=350, y=0)
player2.penup()

# score text============ 
score=turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(x=0, y=260)
score.write("Player1: 0 Player2: 0", align="center", font=("courier",14,"normal"))
score.hideturtle() # we hide object we only want to see the  text
p1_score=0
p2_score=0

#player movement=========
def p1_move_up():
    player1.sety(player1.ycor()+20)

def p2_move_up():
    player2.sety(player2.ycor()+20)

def p1_move_down():
    player1.sety(player1.ycor()-20)

def p2_move_down():
    player2.sety(player2.ycor()-20)


# get user inputs (key bindings)========

window.listen()  # tell the window to expect user inputs 
window.onkeypress(p1_move_up,"w") 
window.onkeypress(p1_move_up,"W") 
window.onkeypress(p1_move_down,"s") 
window.onkeypress(p1_move_down,"S") 

window.onkeypress(p2_move_up,"Up") 
window.onkeypress(p2_move_down,"Down") 

#game loop==================
while(True):
    window.update()
    #boll movement=================
    ball.setx(ball.xcor()+(ball_dx*ball_speed)) #مكانها الحالي مجموع علي  والمقدار الي بتتحرك بيه في اتجاه اكس في السرعه يساوي مكان جديد للكره
    ball.sety(ball.ycor()+(ball_dy*ball_speed))

    #ball & borders collisions ==========
    if(ball.ycor() > 290): #300-10 top border - half ball size 
        ball.sety(290)
        ball_dy *=-1 #invert Y direction 

    if(ball.ycor() < -290): 
        ball.sety(-290)
        ball_dy *=-1

    #ball & players collisions===========
    #collision with player1============

    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()>(player1.ycor()-60) and ball.ycor()<(player1.ycor()+60):
        ball.setx(-340)
        ball_dx*=-1

    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()>(player2.ycor()-60) and ball.ycor()<(player2.ycor()+60):
        ball.setx(340)
        ball_dx*=-1
            
    #score handeling===========
    if(ball.xcor()>390):
        ball.goto(0,0)
        ball_dx*=-1
        score.clear()
        p1_score+=1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center", font=("courier",14,"normal"))

    if(ball.xcor()<-390):
        ball.goto(0,0)
        ball_dx*=-1
        score.clear()
        p2_score+=1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center", font=("courier",14,"normal"))


    
            
