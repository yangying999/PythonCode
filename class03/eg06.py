# 用continue实现打印10以内的偶数
# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(i,end=" ")
# --2--
# for i in range(10):
#     if i % 2 ==0:
#         continue
#     print(i,end=" ")
#
# 打印九九乘法表
# --1--
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end="  ")
#     print()
# --2--
# i = 1
# while i <=9:
#     j=1
#     while j<=i:
#         print(i,"*",j,"=",i*j,end="  ")
#         j += 1
#     i += 1
#     print()
# --3--
# for i in range(1,10):
#     j = 1
#     while j<=i:
#         print(i, "*", j, "=", i * j, end="  ")
#         j += 1
#     print()
# --4--
i = 1
while i <=9:
    for j in range(1,i+1):
        print(i, "*", j, "=", i * j, end="  ")
        # print("%d*%d=%d" %(j,i,i*j),end="\t")
        # print(str(j)+"*"+str(i)+"="+str(i*j),end="\t")
    i += 1
    print()
