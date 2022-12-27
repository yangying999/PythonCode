# while True:
#     try:
#         num = int(input("请输入一个整数："))
#     except ValueError:
#         print("只能输入整数，请重新输入！")
#         continue
#     break
# s = str(num)
# print(s)

#
def process(n):  #参数一定是字符串类型的
    if len(n)== 1:
        return n
    else:
        return n[0]+process(n[1:])
while True:
    try:
        num = int(input("请输入一个整数："))
    except ValueError:
        print("只能输入整数，请重新输入！")
        continue
    break
num = str(num)
s = process(num)
print(s)
s = process(num)