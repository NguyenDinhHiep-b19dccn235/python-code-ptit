def socs(n):
    n=int(n)
    a=0
    while n>0:
        a+=1
        n//=10
    return a
def vitri(n):
    n=str(n)
    a=n[1]
    b=0
    for i in range(1,len(n)):
        if i%2==1:
            if n[i]==a:
                b+=1
            else:b+=0
    if b==0:
        return 0
    else:
        return 1
t=int(input())
while t>0:
    t-=1
    n=input()
    if n[1]!=n[2] and socs(n)%2==1 and vitri(n)==1:
        print('YES')
    else:
        print('NO')