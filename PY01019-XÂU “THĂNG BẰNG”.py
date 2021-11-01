t=int(input())
while t>0:
    t-=1
    n=input()
    n=list(n)
    s=list(n)
    s.reverse()
    a=0
    for i in range(1,len(n)):
        if abs(ord(n[i])-ord(n[i-1]))==abs(ord(s[i])-ord(s[i-1])):
            a+=0
        else:
            a+=1
    if a==0:
        print('YES')
    else:
        print('NO')