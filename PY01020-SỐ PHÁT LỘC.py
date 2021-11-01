t=int(input())
while t>0:
    t-=1
    a=int(input())
    b=a%100
    if b==86:
        print('YES')
    else:
        print('NO')