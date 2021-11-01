t=int(input())
x=t
while t>0:
    t-=1
    s1=input()
    s2=input()
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    a=0
    b=x-t
    if len(s1)==len(s2):
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                a+=1
            else:
                a+=0
        if a==0:
            print('Test ',end='')
            print(b,end='')
            print(':',end=' ')
            print('YES')
        else:
            print('Test ',end='')
            print(b,end='')
            print(':',end=' ')
            print('NO')
    else:
        print('Test ',end='')
        print(b,end='')
        print(':',end=' ')
        print('NO')