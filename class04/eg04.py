# python从键盘输入一个数n,求n的阶乘
# s = 1
# for i in range(1,6):
#     s = s*i
# print(s)
#
# n = int(input("请任意输入一个整数n："))
# s = 1
# for i in range(1,n+1):
#     s = s*i
# print("%d的阶乘为：%d" %(n,s))

#阶乘的累加
# n = int(input("输入n:"))
# s = 0
# for i in range(1, n + 1):
#     # 求j的阶乘，结果在ji中
#     ji = 1
#     for j in range(1, i + 1):
#         ji = ji * j
#     s = s + ji
# print(s)

#
# n=int(input("输入n:"))
s=0
for i in range(1,5):
    ji=1
    for j in range(1,i+1):
        ji=ji*j
    s=s+ji
print(s)
