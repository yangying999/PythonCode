#----1----
h=float(input("身高(m)："))
w=float(input("体重(kg)："))
x= w/(pow(h,2))  # x=w/(h*h)  or  x=w/(h**2)
if x<18.5:
    print("偏瘦")
elif x<24:
    print("正常")
elif x<30:
    print("偏胖")
else:
    print("肥胖")
