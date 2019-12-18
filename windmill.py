from random import randint as r
import time

tom = Turtle()
tom.shape('turtle')
tom.speed(20)
tom.tracer(20)
tom.hideturtle()
tom.width(5)

while True:
    tom.color(r(0,255),r(0,255),r(0,255))
    for k in range(4):
        for i in range(2):
            tom.forward(50)
            tom.right(60)
            tom.forward(100)
            tom.right(120)
        tom.right(90)
    time.sleep(0.3)
    tom.right(10)
    tom.clear()