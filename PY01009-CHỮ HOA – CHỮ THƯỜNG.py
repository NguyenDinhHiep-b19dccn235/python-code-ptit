x=input()
a=0
b=0
for i in x:
    if i.islower():
        a+=1
    else:
        b+=1
if a==b:
    print(x.lower())
elif a>b:
    print(x.lower())
else:
    print(x.upper())

 