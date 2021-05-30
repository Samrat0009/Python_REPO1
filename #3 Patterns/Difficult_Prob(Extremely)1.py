n = int(input())
i = 1
while(i<=(n+1)/2):
    space = ((n+1)/2) - i
    while (space > 0):
        print(end=" ")
        space = space - 1
    j=1
    while(j<=(2*i-1)):
        print('*',end="")
        j= j+1
    print()
    i=i+1
i = (n+1)/2
while(i > 0):
    space = 0
    while (space <= ((n+1)/2)-i):
        print(end=" ")
        space = space + 1
    j=2
    while(j<2*i-1):
        print('*',end="")
        j= j+1
    print()
    i=i-1


#    sample output :

#   *
#  ***
# *****
#*******
# *****
#  ***
#   *