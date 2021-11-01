t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=0
    b=1
    while n>0:
        a=n%10
        n//=10
        if a==0:
            b*=1
        else:b*=a
    print(b)