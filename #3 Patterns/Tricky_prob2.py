## Tricky question:output as follows
##              1
##             212
##            32123
##           4321234

n = int(input())
i = 1
while(i<=n):
    space = n - i
    while (space > 0):
        print(end=" ")
        space = space - 1
    j=i
    #increasing sequence
    while(j>0):
        print(j,end="")
        j= j-1
    #decreasing sequence
    j=2
    while (j <= i):
        print(j, end="")
        j = j + 1
    print()
    i=i+1
