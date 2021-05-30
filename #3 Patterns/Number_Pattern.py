n = int(input())
i=1
while(i<=n):
    p=1
    while(p<=i):
        print(p,end="")
        p=p+1
    j = (n-i)*2-1
    while(j>=0):
        print(' ',end="")
        j=j-1
    p = i
    while (p > 0):
        print(p, end="")
        p = p - 1
    print()
    i=i+1
