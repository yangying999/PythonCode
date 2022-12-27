#50个随机整数，每个整数都在0-20之间
import random
from random import *
# for i in range(50):
#     x = random.randint(10,80)
#     if i % 10 == 0:
#         print("\n")
#     print(x,end="\t")
# 产生小数
# for i in range(5):
#     x = random()
#     print(x)

#100元，100只，公鸡5元/只，母鸡3元/只，小鸡三个1元
# 公鸡i，母鸡j，小鸡100-i-j
# for i in range(100):
#     for j in range(100):
#         if 5*i+3*j+(100-i-j)/3 == 100 and (100-i-j) % 3 == 0:
#             print("公鸡%d只,母鸡%d只，小鸡%d只" %(i,j,100-i-j))

# 输出100内能被7整除但不能被5整除的所有的数
# for i in range(100):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i,end="\t")

# N=100
# s=0
# for i in range(N+1):
#     s = s + 1 / (pow(16, i)) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
# print(s)

# s=1/2+2/3+3/4+4/5+……+n/n+1     n=210
# n = int(input("输入n:"))
# s=0
# for i in range(1,n+1):
#     s =s + i / (i + 1)
# print(s)
#
# 找出100内前五个能被5整出的数
# count=0
# for i in range(100):
#     if i % 5 == 0:
#         print(i,end=" ")
#         count+=1
#         if count == 5:
#             break

# for i in range(5):  #行
#     for j in range(5):  #列
#         print(i,end="\t")
#     print()

# 求阶乘
# s=1
# for i in range(1,5):
#     s = s*i
# print(s)
# 求阶乘累计和
n = int(input("输入n:"))
s = 0
for i in range(1, n + 1):
    # 求j的阶乘，结果在ji中
    ji = 1
    for j in range(1, i + 1):
        ji = ji * j
    s = s + ji
print(s)






