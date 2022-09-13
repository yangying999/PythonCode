#求圆的面积1
r=3.6
s=3.14*r*r
print("面积为："+ str(s))  #用str()函数转换为字符串

#求圆的面积2
import math
# from math import pi
r=float(input("请输入半径："))  #input(),结果是字符串类型，必须转换为数值类型
s=math.pi * r * r
x=math.e
print("面积为："+ str(s)) #用str()函数转换为字符串