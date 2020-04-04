from turtle import *
import time
import random

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
    time.sleep(delay)
