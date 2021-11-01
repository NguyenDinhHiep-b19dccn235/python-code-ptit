def ngto(n):
    a=1
    b=0
    while a<n:
        a+=1
        if n%a==0:
            b+=1
        else: b+=0
    if b==1:
        return 1
    else:
        return 0
def vitri(n):
    n=str(n)
    a=0
    for i in range(0,len(n)):
        if ngto(i)==1 and ngto(int(n[i]))==1:
            a+=0
        elif ngto(i)==0 and ngto(int(n[i]))==0:
            a+=0
        else:
            a+=1
    if a==0:
        return 1
    else: return 0
t=int(input())
while t>0:
    t-=1
    n=int(input())
    if vitri(n)==1:
        print('YES')
    else:
        print('NO')
