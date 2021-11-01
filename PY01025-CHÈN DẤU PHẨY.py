n=input()
i=len(n)-1
dem=0
x=""
while 1:
    dem+=1
    x=n[i]+x
    if i==0: break
    if dem==3:
        x=','+x
        dem=0
    i-=1
print(x)
