def check(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=1
        else:
            a+=0
    if a==1:
        return 1
    else:
        return 0

t=int(input())
while t>0:
    t-=1
    n=input()
    a=int(n[0]+n[1]+n[2])
    b=int(n[-3]+n[-2]+n[-1])
    if check(a)==1 and check(b)==1:
        print('YES')
    else:
        print('NO')