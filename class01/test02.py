#输入三角形的三边长，求其周长
import math
a=float(input("输入第一边的长度："))
b=float(input("输入第二边的长度："))
c=float(input("输入第三边的长度："))
L=math.pi * (a+b+c)
print("周长为：" + str(L))

#如果边长满足任何两边的和 > 第三边
#并且任何两边的差 < 第三边
# if (a+b>c)or(a+c>b)or(b+c>a):
#     if(a-b<c)or(b-c<a)or(a-c<b):
#
#
#     L=math.pi * (a+b+c)
#     print("周长为：" + str(L))