## Tricky question:output as follows
##              1
##             232
##            34543
##           4567654

n = int(input())
i = 1
while(i<=n):
    space = n - i
    while (space > 0):
        print(end=" ")
        space = space - 1
    j=i
    #increasing sequence
    while(j<2*i-1):
        print(j,end="")
        j= j+1
    #decreasing sequence
    while (j >= i):
        print(j, end="")
        j = j - 1
    print()
    i=i+1
