n=input()
s=list(n)
s.reverse()
for i in range(len(s)):
    check=False
    if s[i]=='6':
        check=True
    elif s[i]=='8' and s[i+1]=='6':
        check=True
        if i==len(s)-1:
            break
    elif s[i]=='8' and s[i+1]=='8' and s[i+2]=='6':
        check=True
        if i==len(s)-2:
            break
    if check==False:
        break
if check==False:
    print('NO')
else:
    print('YES')