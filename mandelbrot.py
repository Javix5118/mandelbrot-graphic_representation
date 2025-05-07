import turtle

screen = turtle.Screen()
WIDTH = int(1.75 * 600)  # → 1050
HEIGHT = 600


PIXEL_SIZE = 3
screen.bgcolor("white")
screen.setup(WIDTH, HEIGHT)
screen.title('Mandelbrot - Summa_in_primis')
screen.tracer(0)
t = turtle.Turtle()
t.penup()
RE_START, RE_END = -2.5, 1
IM_START, IM_END = -1, 1
MAX_ITER = 100  # Iteraciones por punto

'''
Este es el algoritmo que determina si un número se encuentra en el conjunto de Mandelbrot o no,
para esto se hace una sucesión hasta MAX_ITER, si el resultado de realizar este algoritmo da
2 se dice que cae hacia el infinito asi que no se considera dentro del conjunto
'''


def mandelbrot(c):
    global n
    z = 0
    for n in range(MAX_ITER):
        z = z ** 2 + c
        if abs(z) > 2:
            return n

    return n


for x in range(-WIDTH // 2, WIDTH // 2, PIXEL_SIZE):
    for y in range(-HEIGHT // 2, HEIGHT // 2, PIXEL_SIZE):
        # Convertir (x, y) a un número complejo c
        re = RE_START + (x + WIDTH // 2) * (RE_END - RE_START) / WIDTH
        im = IM_START + (y + HEIGHT // 2) * (IM_END - IM_START) / HEIGHT
        c = complex(re, im)
        m = mandelbrot(c)
        if mandelbrot(c) == 99:
            t.color('black')
            t.goto(x, y)
            t.dot(PIXEL_SIZE)
        elif mandelbrot(c) != 100:
            if n <= 5:
                t.color('red')
                t.goto(x, y)
                t.dot(PIXEL_SIZE)
            elif n <= 8:
                t.color('yellow')
                t.goto(x, y)
                t.dot(PIXEL_SIZE)
            elif n <= 15:
                t.color('green')
                t.goto(x, y)
                t.dot(PIXEL_SIZE)
            elif n < 100:
                t.color('blue')
                t.goto(x, y)
                t.dot(PIXEL_SIZE)

    counter = 0
    if counter == 100:
        screen.update()
        counter = 0
    counter += 1
    screen.update()

turtle.done()
