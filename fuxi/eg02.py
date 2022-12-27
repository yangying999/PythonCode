d={10067:{'Chi':89,'Math':90,'Eng':89,'Phy':90,'Che':80},
     10068:{'Chi':89,'Math':90,'Eng':85,'Phy':90,'Che':85},
     10069:{'Chi':79,'Math':91,'Eng':80,'Phy':88,'Che':80},
     10070:{'Chi':92,'Math':99,'Eng':90,'Phy':90,'Che':90}}
# 求第一门课的平均分
# vs = d.values()
# s = 0
# for x in vs:
#     s += x.get('Chi')
# aver = s / len(d)
# print(aver)
#
# 找出有两门以上课程不及格的学生，输出他们的学号和全部课程成绩及平均成绩
# for k,v in d.items():    #k--10067;v--{'Chi':89,'Math':60,'Eng':59,'Phy':90,'Che':60}
#     # v = d.get(k)
#     i = 0    #i用来计数（不及格的成绩数）
#     vs = v.values()      #vs--[89,60,59,90,60]
#     for  x in vs:
#         if x<60:
#             i+=1
#     if i>=2:
#         print(k)
#         for y in vs:
#             print(y,end='  ')
#         print()
#         print(f"平均{sum(vs) / len(vs)}")

#  平均>=90 或所有成绩>=85
for k,v in d.items():
    v=d.get(k)
    vs = v.values()
    aver = sum(vs)/len(vs)
    i = 0
    for x in vs:
        if x>=85:
            i +=1

    if aver>=90 or i>=5:
        print(k)
