#simple example: to print all numbers except 29


#n = int(input())
#for i in range(1,n+1,1):
#    if i==29:
#        continue
#    print(i)




#complex example:

# working a condition only for odd numbers:

n = int(input())
for i in range(1,n+1,1):
    if i%2==0:
        continue
    print(i)

# working a condition only for even numbers:


n = int(input())
for i in range(1,n+1,1):
    if i%2!=0:
        continue
    print(i)