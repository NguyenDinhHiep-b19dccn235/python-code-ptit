def dcuoi(n):
    n=str(n)
    a=n[-4]+n[-3]+n[-2]+n[-1]
    b=int(a)
    x=1
    y=0
    while x<b:
        x+=1
        if b%x==0:
            y+=1
        else:
            y+=0
    if y==1:
        return 1
    else:
        return 0
t=int(input())
while t>0:
    t-=1
    n=int(input())
    if dcuoi(n)==1:
        print('YES')
    else:
        print('NO')