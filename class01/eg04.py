from turtle import *  #from库名  import函数名
setup(650,350,200,200)  #显示一个指定大小和位置的窗口
speed(1)
penup()
fd(-250)
pendown()
pensize(20)
pencolor('purple')
seth(-40)
for i in range(4):
    circle(40,80)  #r>0,逆时针画80°的弧
    circle(-40,80)  #r<0,顺时针画弧
circle(40,40)
fd(40)
circle(16,180)
fd(40*2/3)

