#导入turtle库
import turtle
#导入turtle画笔
turtle.shape('turtle')
# turtle.speed(0)
turtle.pencolor('pink')#线条的颜色
length = 150;#定义变量
x = 70;
y = 220;
#面部
turtle.fillcolor('pink')#填充颜色为粉色
turtle.begin_fill()#代码开始填充的地方

#绘制一个length为150的圆。也就是圆的半径为150
turtle.circle(length)

turtle.end_fill()# 代码结束填充的地方
#耳朵
turtle.penup()
turtle.goto(-130,220)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.penup()
turtle.goto(130,220)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

#眉毛
turtle.pencolor('black')
turtle.penup()
turtle.goto(-x,y)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.forward(40)
#眼睛
#右眼
turtle.penup()
turtle.goto(x+20,y-40)
turtle.pendown()
turtle.dot(15,'seashell')
#小眼睛
turtle.penup()
turtle.goto(x+20,y-40)
turtle.pendown()
turtle.dot(5,'black')
#左眼
turtle.penup()
turtle.goto(-x+20,y-40)
turtle.pendown()
turtle.dot(15,'seashell')
#小眼睛
turtle.penup()
turtle.goto(-x+20,y-40)
turtle.pendown()
turtle.dot(5,'black')

#猪鼻子大
turtle.pencolor('pink')
turtle.penup()
turtle.goto(0,70)
turtle.pendown()
turtle.fillcolor('seashell')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#两个小猪鼻子
turtle.penup()
turtle.goto(-15,115)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(25,115)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.hideturtle()