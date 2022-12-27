#切片
a = [10,20,30,40,50,60,70]  #小标从0开始
# b = a[:]       #[10, 20, 30, 40, 50, 60, 70]
# b = a[2:]         #[40, 50, 60, 70]
# b = a[2:6]     #取左不取右  [30, 40, 50, 60]
# b = a[2:6:2]   #[30, 50]
# b = a[-4:]       #[40, 50, 60, 70]
# b = a[:-4]       #[10, 20, 30]
# b = a[-4:-1]      #[40, 50, 60]
# b = a[-4:-1:2]   #[40, 60]
# b = a[-2:-5:-1]  #步长<0时，从右往左  [60, 50, 40]
# b = a[::-1]    #[70, 60, 50, 40, 30, 20, 10]
# print(b)
# aa = a.copy()
# a[0] = 99
# print(aa)
# print("列表的长度是：",len(a),"最大值是：",max(a),"最小值是：",min(a))
# print(a.count(50))

# n=0
# s=[]
# sum=0
# while True:
#     a=input("输入一个工资:")
#     if a.upper()=='Q':
#         break
#     if float(a)<0:
#         continue
#     n+=1
#     s.append(float(a))
#     sum+=float(a)
#     print("个数是%d"%n)
#     print("工资是",s)
#     print("平均工资是：{:.3f}".format(sum/n))


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"*"+str(j)+"="+str(i*j),end="\t")
#     print()

# for i in range(5):
#     for j in range(5):
#         print(i,end="\t")
#     print()

# name1 = ['zhou','yang','li','yan','cheng']
# name2 = ['cao','he','yan','yuan','cheng']
# for x in name2:
#     if x in name1:
#         print(f"{x}已存在，不可添加")
#     else:
#         print(f"{x}可以添加")


list= [1,2,3,4,5,6,7,8,9]
for x in list:
    if x == 1:
        print(f"{x}st")
    elif x == 2:
        print(f"{x}nd")
    elif x == 3:
        print(f"{x}rd")
    else:
        print(f"{x}th",end=' ')