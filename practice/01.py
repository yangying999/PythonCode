# 输入三角形三个顶点的坐标，若有效则计算三角形的面积；若坐标无效，则给出提示

import math

def isvalid(a=0.0, b=0.0, c=0.0):
    """判断三条边长是否符合三角形的定义：任意两边之和大于第三边或者任意两边之差小于第三边"""
    side = [a, b, c]
    side.sort()
    if side[0] + side[1] > side[2] or side[2] - side[1] < side[0]:
        return True
    else:
        return False


def calculate_area():
    """获取三角形的三个顶点坐标并计算该三角形的面积"""
    x1, y1 = map(int, input('请输入第一个顶点坐标：').split())
    x2, y2 = map(int, input('请输入第一个顶点坐标：').split())
    x3, y3 = map(int, input('请输入第一个顶点坐标：').split())

    # 计算三条边长
    side1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    side2 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    side3 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

    # 调用 isvalid() 函数，判断是否能够构成三角形
    if isvalid(side1, side2, side3):
        # 计算半周长
        s = (side1 + side2 + side3) / 2
        # 计算面积
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        print('三角形的面积为：{:.2f}'.format(area))
    else:
        print('坐标无效，无法构成三角形')


if __name__ == '__main__':
    calculate_area()

