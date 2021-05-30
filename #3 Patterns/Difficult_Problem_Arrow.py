n = int(input())
i = 1
while(i<=(n+1)/2):
    space = 1
    while (space < i):
        print(end=" ")
        space = space + 1
    j=1
    while(j<=i):
        print('*',end=" ")
        j= j+1
    print()
    i=i+1
i = (n+1)/2
while(i > 0):
    space = i-1
    while (space > 1):
        print(end=" ")
        space = space - 1
    j=i-1
    while(j>0):
        print('*',end=" ")
        j= j-1
    print()
    i=i-1


#    sample output :

#   *
#    **
#     ***
#      ****
#     ***
#    **
#   *