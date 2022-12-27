score=[{'Chinese':60,'Math':90,'English':95,'Phi':60,'Che':70},
       {'Chinese':70,'Math':80,'English':75,'Phi':66,'Che':60},
       {'Chinese':65,'Math':94,'English':85,'Phi':77,'Che':74},
       {'Chinese':80,'Math':70,'English':65,'Phi':65,'Che':98},
       {'Chinese':69,'Math':80,'English':91,'Phi':70,'Che':69},
       ]
def aver(s):
    for i in range(len(score)):
        sum = 0
        values = score[i].values()
        for v in values:
            sum += v
        print(f"第{i+1}个人的平均分={sum/5}")
aver(score)  #求每个人的平均分

# def aver_course(s):
#     for k in s[2].keys():
#         sum = 0
#         for i in range(len(s)):
#             sum += s[i].get(k)
#         print(f"课程为{k},平均分={sum/len(s)}")
        # print("课程为%s,平均分=%.3f" %(k,sum/len(s)))
# aver_course(score)


# li = []
# for i in range(len(score)):
#     values = score[i].values()
#     li.extend(values)
# MAX = max(li)
# print(MAX)
#
# for i in range(len(score)):
#     for k,v in score[i].items():
#         if v == MAX:
#             print(f"第{i+1}人的{k}课程为最高分，值={MAX}")


####
# print("----------------------------------")
# n = int(input("输入一个四位数： "))
# a=n//1000
# b=(n//100)%10
# c=(n//10)%10
# d=n%10
# s=[a,b,c,d]
# for i in s:
#     print(i,end=' ')
#
# def transfer(n):
#     s=str(n)
#     s2=' '.join(s)
#     print(s2)
# try:
#     n=int(input("请输入一个四位数：  "))
#     transfer(n)
# except ValueError:
#     print("只能输入整数，请重新输入")
# finally:
#     print("结束")

# x = int(input("输入x的值为： "))
# y = int(input("输入y的值为： "))
# s = x/y
# try:
#     print(s)
# except ValueError:
#     print("y为除数不能为0")
# finally:
#     print("结束")

