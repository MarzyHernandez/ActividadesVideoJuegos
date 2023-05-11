from random import *
from turtle import *
from freegames import path

car = path('car.gif')  # Ruta de la imagen del auto
tiles = list(range(32)) * 2  # Lista de números de los pares de fichas
state = {'mark': None}  # Estado actual del juego
hide = [True] * 64  # Lista que indica si las fichas están ocultas o no
tap_count = 0  # Contador de toques en el juego
game_completed = False  # Indicador de si el juego ha sido completado o no

def square(x, y):
    "Dibujar un cuadrado blanco con un borde negro en las coordenadas (x, 
y)."
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
    "Convertir las coordenadas (x, y) a un índice de ficha."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convertir un índice de ficha a coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualizar la ficha marcada y las fichas ocultas según el toque."
    global tap_count, game_completed
    tap_count += 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    if all(not h for h in hide):
        game_completed = True

def draw():
    "Dibujar la imagen y las fichas."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        digit = tiles[mark]
        color(get_color(digit))
        up()
        goto(x + 25, y)
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

    up()
    goto(0, -200)
    color('black')
    write("Número de taps: {}".format(tap_count), align='center', 
font=('Arial', 16, 'normal'))

    if game_completed:
        up()
        goto(0, 0)
        color('red')
        write("¡Todos los cuadros se han destapado!", align='center', 
font=('Arial', 24, 'bold'))

    update()
    ontimer(draw, 100)

def get_color(digit):
    "Devolver el color correspondiente al dígito dado."
    colors = 
['red','blue','green','yellow','orange','purple','brown','black','cyan','magenta','sienna','olive','khaki','silver','indigo','orchid','crimson']
    return colors[digit % len(colors)]

shuffle(tiles)  # Mezclar aleatoriamente las fichas
setup(420, 420, 370, 0)  # Configurar la ventana de Turtle
addshape(car)  # Agregar la forma del auto al sistema de formas de Turtle
hideturtle()  # Ocultar la tortuga
tracer(False)  # Desactivar la animación de dibujo
onscreenclick(tap)  # Asignar la función de respuesta al evento de clic en 
la pantalla
draw()  # Iniciar el juego
done()  # Finalizar la ejecución del programa Turtle

