#画五星红旗
from turtle import *
color('red','red')
begin_fill()  #调用的方法
for i in range(5):
    fd(200)  #前进200
    rt(144)  #右转144，每个角都为36°
end_fill()  #调用的方法