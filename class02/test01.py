import math
#1. 算还款
# total = 700000
# rate = 0.0588/12  #月利率
# year = 10
# pay = (total*rate)/(1-(1/(pow(1+rate,12*year))))
# print("每月应当还%.2f" %pay)

#2. max()  min()
# a = (3,5,23,1,4)
# b = sorted(a,reverse=True)  #reverse=True为从大到小排序
# print(b)

# 3.
# a = float(input("输入第一条边："))
# b = float(input("输入第二条边："))
# c = float(input("输入第三条边："))
# x = (a,b,c)
# y = sorted(x,reverse=True)
# a=y[0]
# b=y[1]
# c=y[2]
# # 如果任何两边的和>第三边 and 任何两边的差<第三边
# if (a+b>c and a+c>b and b+c>a) and (a-b<c and a-c<b and b-c<a):
#     s = a+b+c
# else:
#     print("不能构成三角形")

# F=5/3(C+24.5)

# s=int(input("请输入三位数a的值："))
# x=s/100
# y=(s/10)%10
# z=s%10
# print("a的个位为：%d" %z)
# print("a的十位为：%d" %y)
# print("a的百位为：%d" %x)

# s=int(input("请输入一个四位数："))
# a=s/1000
# b=(s/100)%10
# c=(s/10)%10
# d=s%10
# print("s的千位为：%d" %a)
# print("s的百位为：%d" %b)
# print("s的十位为：%d" %c)
# print("s的个位为：%d" %d)

s=int(input("请输入一个五位数："))
a=s/10000
b=(s/1000)%10
c=(s/100)%10
d=(s/10)%10
e=s%10
print("s的万位为：%d" %a)
print("s的千位为：%d" %b)
print("s的百位为：%d" %c)
print("s的十位为：%d" %d)
print("s的个位为：%d" %e)