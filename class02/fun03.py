# 利用\r在命令行实现转圈功能

import time
lst = ["\\","|","/","——"]
for i in range(20):
    j = i % 4
    print("\r" + lst[j],end="")
    time.sleep(0.2)
