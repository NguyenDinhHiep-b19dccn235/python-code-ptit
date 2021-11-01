t=int(input())
while t>0:
    t-=1
    n=input()
    x=0
    for i in n:
        if int(i)==7:
            x+=0
        elif int(i)==4:
            x+=0
        else:
            x+=1
    if x==0:
        print('YES')
    else:
        print('NO')