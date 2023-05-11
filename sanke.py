from turtle import *
from random import randrange, choice
from freegames import square, vector

colors = ['blue', 'green', 'purple', 'yellow', 'orange']  # Colores disponibles para la serpiente y la comida

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
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
        

    else:
        snake.pop(0)


    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

def move_food():
    "Move food randomly one step"
    global food
    while True:
        direction = vector(randrange(-1, 2, 2)*10, randrange(-1, 2, -2)*10)
        new_food = food + direction
        if inside(new_food):
            food = new_food
            break

snake_color = choice(colors)
available_colors = [c for c in colors if c != snake_color]
food_color = choice(available_colors) if available_colors else 'black'

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
