from random import *
from turtle import *
from freegames import path
from math import *

writer = Turtle(visible=False)
tapper = Turtle(visible=False)
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None,'count': 0,'won':False}
hide = [True] * 64
counter = 0

def square(x, y):  # Función que dibuja los cuadrados en (x,y).
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):  # Función que convierte (x,y) en índice de mosaicos.
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):  # Función que convierte el recuento de mosaicos en coordenadas (x,y).
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):  # Función de marca de actualización y mosaicos ocultos según el toque.
    "Update mark and hidden tiles based on tap."
    if (-200 < x + 50 < 200) and (-200 < y < 200) and not state['won']:
        state['count'] += 1
        writer.undo()
        writer.write(state["count"],font=('Arial', 30, 'normal'))
        spot = index(x + 50, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None
        w = 0
        for i in hide:
            if not i:
                w += 1
        if w == 64:
            writer.up()
            writer.goto(152, 100)
            writer.down()  
            writer.write("You won!!!", font=('Arial', 15, 'normal')) 
            state['won'] = True
            return

def drawNumber(n,size):  # Función que dibuja una figura cuando se descubran los pares.
    "Draw a figure from a number"
    size = size//2
    if n == 0:
        tapper.down()
        tapper.seth(0)
        tapper.circle(size)
    elif n == 1:
        tapper.down()
        tapper.seth(90)
        tapper.forward(size)
    else:
        tapper.down()
        tapper.seth(180/n+180)
        tapper.begin_fill()
        for i in range(n):
            tapper.right(360/n)
            tapper.forward(2*size*sin(pi/n))
        tapper.end_fill()

def draw():  # Función que dibuja la imágen y las losas.
    "Draw image and tiles."
    clear()
    goto(-50, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x - 50, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        tapper.color('black')
        tapper.up()
        tapper.goto(x - 25, y + 5)
        if tiles[mark] < 10:
            drawNumber(tiles[mark],40)
        else:
            tapper.goto(x - 35, y + 15)
            drawNumber(tiles[mark]//10,20)
            tapper.up()
            tapper.goto(x - 15, y + 15)
            drawNumber(tiles[mark]%10,20)
        
    update()
    ontimer(draw, 100)

# Parámetros del juego.
shuffle(tiles)
setup(520, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
writer.up()
writer.goto(152, 150)
writer.down()
writer.color('black')
writer.write(state['count'],font=('Arial', 30, 'normal'))
onscreenclick(tap)
draw()
done()