def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1
 
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
t=int(input())
while t>0:
    t-=1
    a,b=[int(i) for i in input().split()]
    if a>b: a,b=b,a
    res=""
    for i in range(a,b+1):
        res=res + str(fibonacci(i))+" "
    print(res)