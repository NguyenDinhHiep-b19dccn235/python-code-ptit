t=int(input())
while t>0:
    t-=1
    n,x,m=[float(i) for i in input().split()]
    a=0
    while n<=m:
        n=n+n*x/100
        a+=1
    print(a)