#输入10个整数，将其中最小的数与第一个数对换，把最大的数与最后一个数对换。
# def shuru():
#     a = []
#     i = 0
#     while i< 5:
#         try:
#             x = int(input("输入一个数："))
#         except ValueError:
#             print("请重新输入，只能是数据")
#             continue
#         a.append(x)
#         i +=1
#     print(a)
# shuru()

# 写3个函数：1.输入10个数；2.进行处理；3.输出10个数。
a=[-3,21,23,12,34,-45,55,66,22,45]
print(a)
def proc(a):
    m=min(a)
    M=max(a)
    k = a.index(m)
    t = a[0]
    a[0]= a[k]
    a[k] = t
    j=a.index(M)
    t = a[-1]
    a[-1]=a[j]
    a[j]=t
    print(a)
proc(a)
