from random import randrange
from turtle import *
from freegames import vector

# Inicializar la posición de la pelota, velocidad y lista de objetivos
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Responder al toque de la pantalla."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Ajustar la velocidad horizontal y vertical de la pelota (más 
rápido)
        speed.x = (x + 200) / 12  
        speed.y = (y + 200) / 12  

def inside(xy):
    "Devolver True si xy está dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Dibujar la pelota y los objetivos."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Mover la pelota y los objetivos."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Ajustar la velocidad horizontal de los objetivos (más rápido)
        target.x -= 2  

        if not inside(target):
            targets.remove(target)
            y = randrange(-150, 150)
            target.x = 200
            target.y = y
            targets.append(target)

    if inside(ball):
        # Ajustar la gravedad de la pelota (más rápido)
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Eliminar los objetivos que están cerca de la pelota
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50)

# Configuración inicial de la ventana y la tortuga
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


