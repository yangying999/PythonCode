import time

# s = 654
# a = s/100
# b = (s/10)%10
# c = s%10
# print("百位数：%d" %a)
# print("十位数：%d" %b)
# print("个位数：%d" %c)

time.sleep(2)
start = time.time()
x = 0
for i in range(5000000):
    x += 1
end = time.time()
print("花了%f秒" %(end-start))

