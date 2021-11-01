t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort()
    x=0
    for i in range(0,n):
        if a[i]<=b[i]:
            x+=0
        else:x+=1
    if x==0:
        print("YES")
    else:
        print("NO")