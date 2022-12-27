def fa(n,x):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return ((2*n-1)*x-fa(n-1,x)-(n-1)*fa(n-2,x))/n

y=fa(2,1)
print(y)