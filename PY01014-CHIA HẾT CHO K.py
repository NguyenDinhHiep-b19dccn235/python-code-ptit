a, k, n=map(int, input().split())
check=False
b=k
while b<=n:
    if b>a:
        print(b-a, end=" ")
        check=True
    b+=k
if check==False: print(-1)