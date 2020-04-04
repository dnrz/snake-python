from turtle import *
import time
import random

punt = 0
mejor_punt = 0
delay = 0.1
#Configuracion ventana
ven = Screen()
ven.title("Mi primer juego en python")
ven.bgpic("fondo.gif")
ven.setup(width = 800, height = 800)
ven.tracer(0)


#Serpiente
kbza = Turtle()
kbza.speed(0)
kbza.shape("square")
kbza.color("green")
kbza.penup()
kbza.goto(0,0)
kbza.direction = "stop"

#Comida
ven.register_shape("Apple.gif")
food = Turtle("Apple.gif")
food.speed(0)
food.penup()
food.goto(100, 100)

#titulo
linea = Turtle()
linea.color("white")
linea.penup()
linea.setpos(-400,320)
linea.pendown()
linea.forward(800)
linea.hideturtle()
titulo = Turtle()
titulo.speed(0)
titulo.color("white")
titulo.penup()
titulo.hideturtle()
titulo.goto(0,360)
titulo.write("Puntaje: 0        Mejor puntaje: 0", align = "center", font =("Courier",24,"normal"))
#segmentos
segmentos = []

def arriba():
    kbza.direction = "up"
def abajo():
    kbza.direction = "down"
def izq():
    kbza.direction = "left"
def der():
    kbza.direction = "right"

def mov():
    if kbza.direction == "up":
        y = kbza.ycor()
        kbza.sety(y + 20)
    if kbza.direction == "down":
        y = kbza.ycor()
        kbza.sety(y - 20)
    if kbza.direction == "left":
        x = kbza.xcor()
        kbza.setx(x - 20)
    if kbza.direction == "right":
        x = kbza.xcor()
        kbza.setx(x + 20)

ven.listen()
ven.onkeypress(arriba, "Up")
ven.onkeypress(abajo, "Down")
ven.onkeypress(izq, "Left")
ven.onkeypress(der, "Right")

while True:
    ven.update()
    #colision con la pared
    if kbza.xcor() > 380 or kbza.xcor() < -380 or kbza.ycor() > 300 or kbza.ycor() < -380:
        time.sleep(1)
        kbza.goto(0,0)
        kbza.direction = "stop"
        for segmento in segmentos:
            segmento.goto(2000,2000)
        segmentos.clear()
        punt = 0
        titulo.clear()
        titulo.write("Puntaje: {}       Mejor puntaje: {}".format(punt, mejor_punt),
                     align="center", font=("Courier", 24, "normal"))
    #agrega segmentos
    if kbza.distance(food) < 20:
        x = random.randint(-380,380)
        y = random.randint(-380,300)
        food.goto(x,y)
        nuevo_Segmento = Turtle()
        nuevo_Segmento.speed(0)
        nuevo_Segmento.shape("square")
        nuevo_Segmento.color("green")
        nuevo_Segmento.penup()
        segmentos.append(nuevo_Segmento)
        #puntaje
        punt += 10
        if punt > mejor_punt:
            mejor_punt = punt
        titulo.clear()
        titulo.write("Puntaje: {}       Mejor puntaje: {}".format(punt,mejor_punt),
                     align="center", font=("Courier", 24, "normal"))
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = kbza.xcor()
        y = kbza.ycor()
        segmentos[0].goto(x,y)
    mov()

    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(kbza) < 20:
            time.sleep(1)
            kbza.goto(0,0)
            kbza.direction = "stop"
            for segmento in segmentos:
                segmento.goto(2000,2000)
            segmentos.clear()
            punt = 0
            titulo.clear()
            titulo.write("Puntaje: {}       Mejor puntaje: {}".format(punt, mejor_punt),
                     align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
