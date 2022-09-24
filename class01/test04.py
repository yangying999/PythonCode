from turtle import *
pensize(5)
color('red','pink')
begin_fill()
for i in range(4):
    fd(200)
    rt(90)
end_fill()
# 点击窗口关闭程序
window = Screen()
window.exitonclick()