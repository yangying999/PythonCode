# 打印九九乘法表
# 1.
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}x{i}={i*j}\t',end='')
#     print()

# 2.
# i=1
# while i<=9:
#     j=1
#     while(j<=i):
#         print(f'{i}*{j}={i * j}', end='\t')
#         j += 1
#     print('')
#     i += 1

    # print('')
#3.
i=1
while i<=9:
    for j in range(1,i+1):
        print(f'{i}*{j}={i * j}', end=' ')
    i += 1
    print()

