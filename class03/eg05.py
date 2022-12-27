# 初值
# 结束条件
# 循环体
# 循环变量必须改变

# i = 1
# while i<= 5:
#     print(i)
#     i=i+1
#     print("在内部")
#
# print("在外面")

#
# i = 1
# n = 0
# while i<=100:
#     n = i + n
#     i=i+1
# print(n)

#水仙花数
s=int(input("请输入一个三位数："))
a =int(s / 100)
b = int((s / 10) % 10)
c = int(s % 10)
n=a*a*a+b*b*b+c*c*c
if s==n:
    print("%d是水仙花数" %s)
else:
    print("不是水仙花数")
# print(n)
# 三位数水仙花
# i=100
# while i<1000:
#     a = int(i / 100)
#     b = int((i / 10) % 10)
#     c = int(i % 10)
#     if i == a*a*a+b*b*b+c*c*c:
#         print("%d是水仙花数" %i)
#     i=i+1
# 四位数水仙花
# i=1000
# while i<10000:
#     a = int(i / 1000)
#     b = int((i / 100) % 10)
#     c = int((i / 10) % 10)
#     d = int(i % 10)
#     if i == pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4):
#         print("%d是水仙花数" %i)
#     i=i+1
