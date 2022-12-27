# 利用嵌套循环打印九九乘法表
# --1--
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "*", i, "=", i * j, end="  ")
#     print()
# --2--
# i = 1
# while i<10:
#     j = 1
#     while j<=i:
#         print(j, "*", i, "=", i * j, end="  ")
#         j += 1
#     i += 1
#     print()
#--3--
# i = 1
# while i<10:
#     for j in range(1,i+1):
#         print(j, "*", i, "=", i * j, end="  ")
#     i += 1
#     print()
# --4--
for i in range(1,10):
    j = 1
    while j<=i:
        print(j, "*", i, "=", i * j, end="  ")
        j += 1
    print()