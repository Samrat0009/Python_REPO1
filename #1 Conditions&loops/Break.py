# simple break

#i=1
#while i<=10:
#    if i==5:
#        break
#    print(i)
#    i=i+1


#printing prime numbers upto:
#remember a can only start from 2:

a = int(input())
n = int(input())
for i in range(a, n+1, 1):
    for j in range(2,i,1):
        if i%j==0:
            break
        print(i)
        break