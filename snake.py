from turtle import *
import time

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

    mov()
    time.sleep(delay)