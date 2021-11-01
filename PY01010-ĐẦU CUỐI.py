t=int(input())
while t>0:
    t-=1
    n=input()
    a=int(n[0]+n[1])
    b=int(n[-2]+n[-1])
    if a==b:
        print('YES')
    else:
        print('NO')