from PIL import Image

#image = Image.open("E:\\Programming\\PycharmProjects\\test\\1.jpg")
#image.show()

import os
import turtle
#turtle.ondrag(turtle.goto)

from matplotlib import pyplot as plt
import numpy as np

size = 2
x = np.linspace(-size, size, 400)
#print(x)

#参考函数 http://www.guokr.com/post/498800/
plt.plot(x, np.sqrt(1-(np.abs(x)-1)*(np.abs(x)-1)))
plt.plot(x, np.arccos(1-np.abs(x))-np.pi)
#plt.show()

#print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

import turtle

def branch(length, level):
    if level <= 0:
        return

    turtle.forward(length)
    turtle.left(45)
    branch(0.6 * length, level - 1)
    turtle.right(90)
    branch(0.6 * length, level - 1)
    turtle.left(45)
    turtle.backward(length)
    return


turtle.hideturtle()
#turtle.Turtle().screen.delay(0)
turtle.left(90)
branch(100, 6)
