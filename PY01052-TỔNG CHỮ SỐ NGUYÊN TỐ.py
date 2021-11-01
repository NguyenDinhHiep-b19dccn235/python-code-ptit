def tongcs(n):
    a=0
    while n>0:
        a+=n%10
        n//=10
    return a
def nguyento(n):
    i=1
    a=0
    while i<=n:
        i+=1
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
    n=int(input())
    a=tongcs(n)
    if nguyento(a)==1:
        print('YES')
    else:
        print('NO')