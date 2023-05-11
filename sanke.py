from turtle import *
from random import randrange, choice
from freegames import square, vector

colors = ['blue', 'green', 'purple', 'yellow', 'orange']  # Colores 
disponibles para la serpiente y la comida

food = vector(0, 0)  # Posición inicial de la comida
snake = [vector(10, 0)]  # Posición inicial de la serpiente
aim = vector(0, -10)  # Dirección inicial de la serpiente
snake_color = ''  # Color de la serpiente
food_color = ''  # Color de la comida

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    # Verifica si la cabeza de la serpiente está dentro de los límites del 
tablero
    return -200 < head.x < 190 and -200 < head.y < 190

def choose_snake_color():
    "Choose a random color for the snake."
    # Elige un color aleatorio para la serpiente de entre los colores 
disponibles,
    # excluyendo el color de la comida actual
    return choice([color for color in colors if color != food_color])

def choose_food_color():
    "Choose a random color for the food."
    # Elige un color aleatorio para la comida de entre los colores 
disponibles,
    # excluyendo el color de la serpiente actual
    return choice([color for color in colors if color != snake_color])

def move():
    "Move snake forward one segment."
    global snake_color, food_color
    
    head = snake[-1].copy()  # Copia la posición de la cabeza de la 
serpiente
    head.move(aim)  # Mueve la cabeza en la dirección actual

    if not inside(head) or head in snake:
        # Si la cabeza está fuera de los límites o colisiona con el cuerpo 
de la serpiente,
        # se muestra la cabeza en rojo y se finaliza el juego
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)  # Agrega la nueva posición de la cabeza a la 
serpiente

    if head == food:
        # Si la cabeza alcanza la comida,
        # se incrementa la longitud de la serpiente, se genera una nueva 
posición aleatoria para la comida
        # y se eligen nuevos colores para la serpiente y la comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        snake_color = choose_snake_color()
        food_color = choose_food_color()

    else:
        snake.pop(0)  # Si la cabeza no alcanza la comida, se elimina la 
cola de la serpiente

    clear()

    for body in snake:
        # Dibuja cada segmento del cuerpo de la serpiente con el color 
correspondiente
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)  # Dibuja la comida con el color 
correspondiente
    update()
    ontimer(move, 100)  # Programa el siguiente movimiento de la serpiente 
después de un tiempo determinado (100 ms)

snake_color = choose_snake_color()
food_color = choose_food_color()

setup(420, 420, 370, 0) # Configura la ventana de juego
hideturtle() # Oculta la flecha del cursor
tracer(False) # Desactiva la animación
listen() # Habilita la escucha de eventos de teclado
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move() # Inicia el movimiento de la serpiente
done() # Finaliza el juego de la tortuga

