# while True:
#     x = int(input("输入x:  "))
#     y = int(input("输入y:  "))
#     try:
#         z = x / y
#         print(z)
#         break
#     except ValueError:
#         print("只能是数据，请重新输入！")
#     except ZeroDivisionError:
#         print("输入y不能为0!")

#
while True:
    try:
        x = int(input("输入x:  "))
    except ValueError:
        print("只能是数据，请重新输入！")
        continue
    while True:
        try:
            y = int(input("输入y:  "))
            z = x / y
            print(z)
            break
        except ZeroDivisionError:
            print("输入y不能为0!")
        except ValueError:
            print("只能是数据，请重新输入！")
        # break
    break


