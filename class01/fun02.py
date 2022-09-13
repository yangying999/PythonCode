from turtle import *

pensize(1)  #画笔宽度
pencolor('red')  #画笔颜色
fillcolor('pink')  #填充颜色
speed(1)  #设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快
penup()
goto(-30,100)  #定点画笔坐标位置
pendown()
begin_fill()  #开始填充
left(90)
circle(100,180)
circle(300,70)
left(38)
circle(300,70)
circle(100,180)
end_fill()
# up()
# goto(-100,-100)
# down()

# turtle画笔控制函数：
#
# turtle.penup():表示抬起画笔，海龟在飞行；可以简写成turtle.pu()
#
# turtle.pendown():表示画笔落下，海龟在爬行；可以简写成turtle.pd()
#
# turttle.pensize(width):表示画笔的宽度，也可以使用turtle.width(width)
#
# turtle.pencolor(color):color为颜色字符串或者 RGB值；
#
# turtle.forward(d):向前行进距离；可以简写为turtle.fd(d)，d为整数可以为负数；
#
# turtle.circle(r,extent=NONE):根据半径r绘制extent角度的弧形，r默认在圆心左侧R距离的位置；extent:绘制角度默认360度是整圆；
