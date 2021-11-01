def ngtocn(a,b):
    a=int(a)
    b=int(b)
    x=0
    while b>0:
        x=a%b
        a=b
        b=x
    return a
t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=n
    m=""
    while a>0:
        m+=str(a%10)
        a//=10
    b=int(m)
    if ngtocn(n,b)==1:
        print('YES')
    else:
        print('NO')
