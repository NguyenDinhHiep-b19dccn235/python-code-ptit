n=input()
x=0
for i in n:
    if int(i)==7:
        x+=1
    elif int(i)==4:
        x+=1
    else:
        x+=0
if x==7:
    print('YES')
elif x==4:
    print('YES')
else:
    print('NO')