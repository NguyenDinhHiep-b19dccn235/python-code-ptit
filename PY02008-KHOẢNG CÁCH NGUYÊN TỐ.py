import math
def ngto(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return 0
    return 1
n,x=[int(i) for i in input().split()]
i=1
dem=0
print(x,end=' ')
while dem<n:
    i+=1
    if ngto(i)==1:
        x+=i
        dem+=1
        print(x,end=' ')


    
