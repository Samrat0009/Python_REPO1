#code square pattern

n = int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(n,end="")
        j=j+1
    print()
    i=i+1

# triangle pattern

n = int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print('1',end="")
        j=j+1
    print()
    i=i+1
