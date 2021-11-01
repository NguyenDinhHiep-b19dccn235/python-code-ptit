a=input()
if len(a)==9:
    b=a[0]
    c=a[4]
    d=a[8]
    if int(b)+int(c)==int(d):
        print('YES')
    else:
        print('NO')