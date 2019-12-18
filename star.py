from random import randint as r

tom = Turtle()
tom.shape('turtle')
tom.speed(10)
tom.tracer(20)
def draw(l):
    tom.width(2)
    for i in range(10):
        tom.color(r(0,255),r(0,255),r(0,255))
        for k in range(7):
            tom.forward(l)
            tom.backward(l)
            tom.left(360.0/7)
        tom.left(360.0/10)
        l += 5

    tom.color('black')
    tom.width(4)
    for i in range(10):
        for k in range(7):
            tom.forward(l)
            tom.backward(l)
            tom.right(360.0/7)
        tom.right(360.0/10)
        l -= 5
        
while True:
    draw(r(20,50))