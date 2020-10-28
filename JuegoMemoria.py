from random import *
from turtle import *
from freegames import path

# Parámetro nuevo (writer)
writer = Turtle(visible=False)
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None,'count': 0,'won':False}
hide = [True] * 64
# contador
counter = 0

def square(x, y):
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

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Función que muestra el número de los pares en las fichas.
# Te despliega todos los "toques" que llevas al no encontrar el par.
def tap(x, y):
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
# Cuando se destapan todos los taps, muestra un mensaje final.
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

def draw():
    "Draw image and tiles."
    clear()
    goto(-50, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
# Nuevo tamaño.
            square(x - 50, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x -48, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(520, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
# Nuevo.
writer.up()
writer.goto(152, 150)
writer.down()
writer.color('black')
writer.write(state['count'],font=('Arial', 30, 'normal'))
onscreenclick(tap)
draw()
done()
