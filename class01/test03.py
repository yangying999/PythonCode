import math
price = float(input("输入单价："))
num   = float(input("输入重量："))
total = float(price * num)
print("单价是：%.2f 元/斤,重量是：%.2f 公斤,总价为：%.2f 元" %(price,num,total))