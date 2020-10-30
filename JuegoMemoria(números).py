from random import *
from turtle import *
from freegames import path

writer = Turtle(visible=False)
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

def xy(count):  # Función que convierte el recuento de mosaicos en coordenadas (x,y)
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
        up()
        if tiles[mark] < 10:
            goto(x - 34, y + 2)
        elif tiles[mark] < 20:
            goto(x - 47, y + 2)
        else:
            goto(x - 45, y + 2)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

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