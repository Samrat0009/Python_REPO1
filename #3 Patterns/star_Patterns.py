

n = int(input())
i = 1
while(i<=n):
    space = n - i
    while (space > 0):
        print(end=" ")
        space = space - 1
    j=1
    while(j<=(2*i-1)):
        print('*',end="")
        j= j+1
    print()
    i=i+1

