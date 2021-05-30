# output:

#        1
#       232
#      34543
#     4567654


n = int(input())

for i in range(1,n+1,1):
    for space in range(1,(n+1)-i,1):
        print(' ',end="")
    for j in range(i,i*2,1):
        print(j,end="")
    for j in range(2*i-2,i-1,-1):
        print(j,end="")
    print()
