import time

for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)

    # \r  ==》  表示将光标的位置回退到本行的开头位置