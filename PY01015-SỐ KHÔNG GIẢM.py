t=int(input())
while t>0:
    t-=1
    a=input()
    b=len(a)
    x=0
    for i in range(0,b-1):
        for j in range(i+1,b):
            if a[i]>a[j]:
                x+=1
            else: 
                x+=0
    if x==0:
        print('YES')
    else:
        print('NO')
 