import turtle 
#Ventana
wn =turtle.Screen()
wn.title("Pong By Fertch")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#JugadorA

jugadorA= turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5,stretch_len=1)


#JugadorB


jugadorB= turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(+350,0)
jugadorB.shapesize(stretch_wid=5,stretch_len=1)


#Pelota

Pelota= turtle.Turtle()
Pelota.speed(0)
Pelota.shape("square")
Pelota.color("white")
Pelota.penup()
Pelota.goto(0,0)
Pelota.shapesize(stretch_wid=1,stretch_len=1)
Pelota.dx = 0.5
Pelota.dy = 0.5


#LineaDivisionb


Linea= turtle.Turtle()
Linea.color("white")
Linea.goto(0,400)
Linea.goto(0,-400)


#marcador
marcadorA=0
marcadorB=0

#Pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write( "JugadorA: 0      JugadorB: 0", align="center",font=("Courier",24,"normal") )

#funciones
#jugadorA
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

#jugadorB
def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_down, "Down")








while True:
    wn.update()

    Pelota.setx(Pelota.xcor()+ Pelota.dx)
    Pelota.sety(Pelota.ycor()+ Pelota.dy)

    #Bordes
    if Pelota.ycor() > 290:
        Pelota.dy *= -1
    if Pelota.ycor() < -290:
        Pelota.dy *=-1

    #bordes derecha/izquierda
    if Pelota.xcor()> 390:
        Pelota.goto(0,0)
        Pelota.dx *=-1
        marcadorA+=1
        pen.clear()
        pen.write( "JugadorA: {}      JugadorB: {}".format(marcadorA,marcadorB), align="center",font=("Courier",24,"normal") )

    if Pelota.xcor()< -390:
        Pelota.goto(0,0)
        Pelota.dx *=-1
        marcadorB+=1
        pen.clear()
        pen.write( "JugadorA: {}      JugadorB: {}".format(marcadorA,marcadorB), align="center",font=("Courier",24,"normal") )

    "coliciones"
    if (Pelota.xcor() >340 and Pelota.xcor() < 350 
        and (Pelota.ycor() < jugadorB.ycor()+ 50
        and Pelota.ycor() > jugadorB.ycor()-50)):
        Pelota.dx*=-1
      

    if (Pelota.xcor() <-340 and Pelota.xcor() >-350 
        and (Pelota.ycor() < jugadorA.ycor()+ 50
        and Pelota.ycor() > jugadorA.ycor()-50)):
        Pelota.dx *= -1
        

    