# Importar librerías necesarias
from random import choice
from turtle import *
from freegames import floor, vector

# Estado del juego
state = {'score': 0}
# Inicialización de los elementos del juego
path = Turtle(visible=False)  # Camino que sigue el personaje
writer = Turtle(visible=False)  # Texto para mostrar la puntuación
aim = vector(5, 0)  # Dirección inicial de Pacman
pacman = vector(-40, -80)  # Posición inicial de Pacman
ghosts = [
    [vector(-180, 160), vector(5, 0)],  # Fantasma 1: posición y dirección
    [vector(-180, -160), vector(0, 5)],  # Fantasma 2: posición y 
dirección
    [vector(100, 160), vector(0, -5)],  # Fantasma 3: posición y dirección
    [vector(100, -160), vector(-5, 0)],  # Fantasma 4: posición y 
dirección
]
tiles = [
    # Diseño del laberinto (0: pared, 1: camino)
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def distance(p1, p2):
    "Return the Manhattan distance between two points."
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) 

def square(x, y):
    "Draw square using path at (x, y)."
    path.up()   # Levanta el lápiz
    path.goto(x, y)   # Mueve el lápiz a las coordenadas (x, y)
    path.down()   # Baja el lápiz para dibujar
    path.begin_fill()   # Inicia el relleno

    for count in range(4):
        path.forward(20)   # Avanza 20 unidades hacia adelante
        path.left(90)   # Gira 90 grados a la izquierda

    path.end_fill()   # Finaliza el relleno

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20   # Calcula la coordenada x en la 
matriz de casillas
    y = (180 - floor(point.y, 20)) / 20   # Calcula la coordenada y en la 
matriz de casillas
    index = int(x + y * 20)   # Calcula el índice correspondiente en la 
matriz de casillas
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0: # Valor en el índice de la matriz de casillas es 
0
        return False

    index = offset(point + 19)

    if tiles[index] == 0: # Valor en el índice de la matriz de casillas es 
0
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200 # Calcula la coordenada x del 
cuadrado en el mundo
            y = 180 - (index // 20) * 20# Calcula la coordenada y del 
cuadrado en el mundo

            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    "Move pacman and all ghosts."
    writer.undo() # Borra el marcador de puntuación
    writer.write(state['score']) # Escribe la puntuación actual en el 
marcador

    clear() # Limpia la pantalla

    if valid(pacman + aim):   # Si el siguiente movimiento del pacman es 
válido
        pacman.move(aim)   # Mueve al pacman en la dirección actual

    index = offset(pacman)   # Obtiene el índice correspondiente al punto 
del pacman

    if tiles[index] == 1:   
        tiles[index] = 2  
        state['score'] += 1   # Incrementa la puntuación en 1
        x = (index % 20) * 20 - 200   # Calcula la coordenada x del 
cuadrado en el mundo
        y = 180 - (index // 20) * 20   # Calcula la coordenada y del 
cuadrado en el mundo
        square(x, y)  

    up()
    goto(pacman.x + 10, pacman.y + 10)   
    dot(20, 'yellow')  

    for ghost in ghosts:
        point, course = ghost
        if valid(point + course):   # Si el siguiente movimiento del 
fantasma es válido
            point.move(course)   # Mueve al fantasma en la dirección 
actual
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            best_option = None
            min_distance = float('inf')

            for option in options:
                if valid(point + option):   # Si el movimiento de opción 
es válido
                    target = pacman   # Establece al pacman como el 
objetivo
                    dist = abs(target - (point + option))   # Calcula la 
distancia al objetivo

                    if dist < min_distance:
                        min_distance = dist
                        best_option = option

            if best_option is not None:   # Si se encontró una mejor 
opción de movimiento
                course.x = best_option.x   # Actualiza la dirección x del 
fantasma
                course.y = best_option.y   # Actualiza la dirección y del 
fantasma

        up()
        goto(point.x + 10, point.y + 10)  
        dot(20, 'red')  

    update()

    for ghost in ghosts:
        point, _ = ghost
        if abs(pacman - point) < 20:
            return

    ontimer(move, 50)



def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()

