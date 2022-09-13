# 利用\r在命令行实现倒计时功能

import time
for i in range(10):
    print("\r倒计时%s秒" % (9-i),end="")
    time.sleep(1)