def tongcs(n):
    a=0
    while n>0:
        a+=n%10
        n//=10
    return a
def thuannghich(n):
    n=str(n)
    a=[int(i) for i in n]
    b=a.copy()
    b.reverse()
    if a==b:
        return 1
    else:
        return 0
 
t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=tongcs(n)
    if a>=10:
        if thuannghich(a)==1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
