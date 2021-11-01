def chan(n):
    n=str(n)
    a=0
    for i in range(0,len(n)):
        if i%2==0:
            if int(n[i])%2==0:
                a+=1
            else:
                a+=0
    if a==0:
        return 0
    else: return 1
def le(n):
    n=str(n)
    a=0
    for i in range(0,len(n)):
        if i%2==1:
            if int(n[i])%2==1:
                a+=1
            else:
                a+=0
    if a==0:
        return 0
    else: return 1
def tongnt(n):
    a=0
    while n>0:
        a+=n%10
        n//=10
    i=1
    b=0
    while i<a:
        i+=1
        if a%i==0:
            b+=1
        else:
            b+=0
    if b==1:
        return 1
    else: return 0
t=int(input())
while t>0:
    t-=1
    n=int(input())
    if chan(n)==1 and le(n)==1 and tongnt(n)==1:
        print('YES')
    else:
        print('NO')
