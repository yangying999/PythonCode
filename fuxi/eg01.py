while True:
    try:
        n=int(input("输入1-12之间的数字："))
    except ValueError:
        print("非法输入，请重新输入！")
        continue
    if n == 1:
        print("January")
    elif n == 2:
        print("February")
    elif n == 3:
        print("March")
    elif n == 4:
        print("April")
    elif n == 5:
        print("May")
    elif n == 6:
        print("June")
    elif n == 7:
        print("July")
    elif n == 8:
        print("August ")
    elif n == 9:
        print("September")
    elif n == 10:
        print("October")
    elif n == 11:
        print("November ")
    elif n == 12:
        print("December")
    else:
        print("输入不符合要求，请重新输入！")
        continue
    break