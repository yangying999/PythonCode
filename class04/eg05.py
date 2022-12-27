# def sss():
#     for i in range(5):
#         for j in range(5):
#             print(i,end=' ')
#         print()
# sss()
###
def jieche(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
# x = jieche(6)
# print(x)
n = int(input("输入n:    "))
s = 0
for i in range(1,n+1):
    s=s+jieche(i)
print(f"1!+2!+3!+……+n! = {s}")
###
# def jieche():
#     n = int(input("输入n："))
#     s = 0
#     for i in range(1,n+1):
#         ji = 1
#         for j in range(1,i+1):
#             ji =ji*j
#         s = s+ji
#     print("%d的阶乘和为：%d" %(n,s))
# jieche()
