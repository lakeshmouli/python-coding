n=int(input())
while True:
    print(n,end=" ")
    if n==1:
        break
    if n%2:
        n=n*3+1
    else:
        n=n//2
