#使用海龟绘图，绘制18*18棋盘
import turtle
t = turtle.Pen()
t.width(2)

for i in range(0, 19):
    t.penup()
    t.goto(0, 15*i)
    t.pendown()
    t.forward(18*15)
t.left(90)
for i in range(0, 19):
    t.penup()
    t.goto(15*i, 0)
    t.pendown()
    t.forward(18*15)
turtle.done()




