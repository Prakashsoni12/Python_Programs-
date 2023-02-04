import turtle
t = turtle.Turtle()
t.screen.bgcolor('white')
t.pensize(2)
t.color('cyan')
t.left(90)
t.backward(100)
t.speed(100)
t.shape('turtle')

def tree(i):
    if i <10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color('red')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()