
#heart

#from turtle import *
import turtle
#from time import sleep
import time
import os

SPEED = 0

def go_to(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def big_Circle(size):  #函数用于绘制心的大圆
    turtle.speed(SPEED)
    # turtle.Turtle().screen.delay(0)
    turtle.getscreen().tracer(1, 0)
    for i in range(150):
        turtle.forward(size)
        turtle.right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
    turtle.speed(SPEED)
    #turtle.Turtle().screen.delay(0)
    turtle.getscreen().tracer(1, 0)
    for i in range(210):
        turtle.forward(size)
        turtle.right(0.786)

def line(size):
    turtle.speed(SPEED)
    turtle.forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   turtle.left(150)
   turtle.begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   turtle.left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   turtle.end_fill()

def arrow():
    turtle.pensize(10)
    turtle.speed(1)
    turtle.getscreen().tracer(1, 2)
    turtle.color('yellow')
    turtle.setheading(0)
    go_to(-500, -50)   #(-400, 0)
    turtle.left(15)
    turtle.forward(430)
    go_to(115, 114)
    turtle.forward(50)
    go_to(319, 170)
    turtle.forward(150)

def arrowHead():
    turtle.pensize(1)
    turtle.speed(1)
    turtle.getscreen().tracer(1, 0)
    turtle.color('wheat', 'yellow')
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(30)
    turtle.right(150)
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(150)
    turtle.forward(25)
    turtle.end_fill()

def flower(size):
    turtle.color("red", "yellow")
    turtle.speed(10)
    turtle.begin_fill()
    for _ in range(50):
        turtle.forward(size) #200
        turtle.left(85)    #170
    turtle.end_fill()

def branch(length, level):
    if level <= 0:
        return
    turtle.pensize(6)
    turtle.forward(length)
    turtle.left(45)
    branch(0.6 * length, level - 1)
    turtle.right(90)
    branch(0.6 * length, level - 1)
    turtle.left(45)
    turtle.backward(length)
    time.sleep(0.02)
    return

def main():
    turtle.hideturtle()
    turtle.pensize(8)
    turtle.color('wheat', 'tomato')
    # red orange yellow green blue purple pink white black
    # brown 棕 grey 灰 beige 米色 brown 褐/茶色 khaki 卡其
    # navy 丈青 palegoldenrod 苍麒麟色 paleturquoise 苍绿
    # palegreen 苍绿 plum 杨李色 peru 秘鲁色 peachpuff 桃色
	# palevioletred 苍紫罗蓝 papayawhip 番木色 salmon 鲜肉色
	# powderblue 粉蓝 rosybrown 褐玫瑰红 royalblue 宝蓝
	# saddlebrown 重褐 sandybrown 沙褐 seashell 海贝
	# seagreen 海绿 silver 银白 slategray 灰石 sienna 赭色
	# skyblue 天蓝 slateblue 石蓝 snow 雪白 gray 烟灰
	# springgreen 春绿 steelblue 钢蓝 tan 茶色 teal 水鸭色
	# thistle 蓟色 tomato 番茄色 turquoise 青绿 violet 粉紫
	# wheat 土黄 whitesmoke 烟白 yellowgreen 黄绿 gold 金
	# olive 橄榄色 coral 珊瑚色 fuchsia 粉玫 chocolate 红褐
	# maroon 褐红色 lavender 淡紫色 ivory 象牙色

    time.sleep(3)
    # turtle.getscreen().tracer(30, 0) #(30, 0)取消注释后，快速显示图案

    heart(150, -20, 1.2)          #(200, 0, 1)画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    turtle.setheading(0)      #使画笔的方向朝向x轴正方向
    heart(-80, -100, 1.4)     #(-80, -100, 1.5)画出第二颗心

    time.sleep(1)
    arrow()                   #画出穿过两颗心的直线
    arrowHead()               #画出箭的箭头

    time.sleep(1)
    turtle.color('skyblue')
    # skyblue turquoise palevioletred
    turtle.getscreen().tracer(3, 2)
    go_to(450, -250)
    turtle.left(90-75)
    branch(140, 9)

    time.sleep(1)
    go_to(-550, -160)
    turtle.pensize(1)
    flower(50)

    FONT = 22; cha = 30; TIME = 4; START = 190
    go_to(-500, -150)          #(400, -300)
    turtle.color('sienna')
    time.sleep(2)
    turtle.write("打字的位置",
                 move=False, align="left",font=("方正舒体", FONT, "normal"))
    time.sleep(TIME)
    go_to(-300, -150)
    turtle.write("同上",
                 move=False, align="left",font=("方正舒体", FONT, "normal"))
    time.sleep(TIME)
    go_to(-450, -START)
    turtle.write("同上",
                 align="left",font=("方正舒体", FONT, "normal"))
    time.sleep(TIME)
    go_to(-450, -START-cha)
    turtle.write("同上",
                 align = "left", font = ("方正舒体", FONT, "normal"))
    time.sleep(TIME+1)
    go_to(-450, -START-2*cha)
    turtle.write("同上",
                 align="left",font=("方正舒体", FONT, "normal"))
    time.sleep(TIME+2)
    go_to(-450, -START-3*cha)
    turtle.write("同上",
                 align="left", font=("方正舒体", FONT, "normal"))
    time.sleep(TIME+1)
    go_to(-450, -START-4*cha-10)
    turtle.write("同上",
                 align="left",font=("方正舒体", FONT-3, "normal"))
    # Vivaldi，华文行楷、彩云、新魏，隶书，方正舒体

    turtle.done()

if __name__ == '__main__':
    main()