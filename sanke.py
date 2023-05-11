from turtle import *
from random import randrange, choice
from freegames import square, vector

colors = ['blue', 'green', 'purple', 'yellow', 'orange']  # Colores 
disponibles para la serpiente y la comida

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
snake_color = ''
food_color = ''

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def choose_snake_color():
    "Choose a random color for the snake."
    return choice([color for color in colors if color != food_color])

def choose_food_color():
    "Choose a random color for the food."
    return choice([color for color in colors if color != snake_color])

def move():
    "Move snake forward one segment."
    global snake_color, food_color
    
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        snake_color = choose_snake_color()
        food_color = choose_food_color()

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

snake_color = choose_snake_color()
food_color = choose_food_color()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
