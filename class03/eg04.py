#------1------
# x=20
# if x<1:
#     y = x
# elif x<10:  #x>=1 and x<10 or 1<=x<10 这两种写法都不对
#     y = 2 * x - 1
# else:
#     y = 3 * x - 11
# print(y)
#------2------
# x=float(input("输入x的值为："))
# if x<10:
#     if x<1:
#         y = x
#     else:
#         y = 2 * x - 1
# else:
#     y=3*x-11
# print("y 的值为：%.1f" %y)
#------3------
x=float(input("输入x的值为："))
if x>10:
    y=3*x-11
else:
    if x>=1:
        y=2*x-1
    else:
        y=x
print(y)
