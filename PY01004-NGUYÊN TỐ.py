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
    n=int(input())
    m=0
    for i in range(1,n+1):
        if ucln(n,i)==1:
            m+=1
    b=0
    c=0
    while b<=m:
        b+=1
        if m%b==0:
            c+=1
    if c==2:
        print('YES')
    else:
        print('NO')