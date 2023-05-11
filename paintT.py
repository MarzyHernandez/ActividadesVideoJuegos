from turtle import *
from freegames import vector

# Función para dibujar una línea desde el punto de inicio hasta el punto 
final.
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado desde el punto de inicio hasta el punto 
final.
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función para dibujar un círculo desde el punto de inicio hasta el punto 
final.
def circulo(start, end):
    """Draw circle from start to end."""
    up()
    radius = abs(start - end)
    goto(start.x, start.y - radius)
    down()
    fillcolor('royal blue')
    begin_fill()
    circle(radius)
    end_fill()

# Función para dibujar un rectángulo desde el punto de inicio hasta el 
punto final.
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    
    end_fill()

# Función para dibujar un triángulo desde el punto de inicio hasta el 
punto final.
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)
    
    end_fill()

# Función que se llama cuando se hace clic en la pantalla.
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Función para almacenar un valor en el estado (diccionario) en una clave 
específica.
def store(key, value):
    """Store value in state at key."""
    state[key] = value

state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)  # Configura el tamaño y la posición de la ventana 
de dibujo
onscreenclick(tap)  # Llama a la función 'tap' cuando se hace clic en la 
pantalla
listen()  # Escucha los eventos del teclado
onkey(undo, 'u')  # Llama a la función 'undo' cuando se presiona la tecla 
'u'

# Configuramos una serie de funciones lambda para cambiar el color del 
trazo cuando se presionen ciertas teclas
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color('cyan'), 'C')
onkey(lambda: color('magenta'), 'M')
onkey(lambda: color('pink'), 'I')
onkey(lambda: color('sienna'), 'S')

# Configuramos una serie de funciones lambda para almacenar diferentes 
formas cuando se presionen ciertas teclas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()  # Finalizamos

