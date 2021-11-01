def tong(n):
    n=str(n)
    a=0
    for i in range(0,len(n)):
        if i%2==0:
            a+=int(n[i])
    return a
def tich(n):
    n=str(n)
    a=1
    for i in range(0,len(n)):
        if i%2==1:
            if int(n[i])>0:
                a=a*int(n[i])
    if a==1:
        return 0
    else:
        return a
t=int(input())
while t>0:
    t-=1
    n= int(input())
    print(tong(n),end=" ")
    print(tich(n))