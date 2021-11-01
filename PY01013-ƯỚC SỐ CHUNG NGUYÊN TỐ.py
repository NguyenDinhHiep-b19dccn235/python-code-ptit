def ucln(n,i):
    a=0
    while i>0:
        n=n%i
        a=n
        n=i
        i=a
    return n
t=int(input())
while t>0:
    t-=1
    a,b=[int(i) for i in input().split()]
    c=ucln(a,b)
    x=0
    while c>0:
        x+=c%10
        c=int(c/10)
    i=0
    y=0
    while i<=x:
        i+=1
        if x%i==0:
            y+=1
    if y==2:
        print('YES')
    else:
        print('NO')