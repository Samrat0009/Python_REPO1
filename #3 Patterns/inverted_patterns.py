## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while(i<=n):
    space = n - i
    while (space > 0):
        print(end=" ")
        space = space - 1
    j=1
    while(j<=i):
        print(j,end="")
        j= j+1
    print()
    i=i+1
