def cso(n):
    n=int(n)
    a=0
    while n>0:
        a+=1
        n//=10
    x=1
    b=0
    while x<a:
        x+=1
        if a%x==0:
            b+=1
        else:
            b+=0
    if b==1:return 1
    else:return 0
def solg(n):
    n=str(n)
    x=0
    y=0
    for i in range(0,len(n)):
        a=int(n[i])
        b=1
        c=0
        while b<a:
            b+=1
            if a%b==0:
                c+=1
            else:c+=0
        if c==1:
            x+=1
        else:y+=1
    if x>y:
        return 1
    else:return 0
t=int(input())
while t>0:
    t-=1
    n=int(input())
    if cso(n)==1 and solg(n)==1:
        print('YES')
    else:
        print('NO')