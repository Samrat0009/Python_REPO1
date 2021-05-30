# check if no. is prime:

n = int(input())
flag = False
for i in range(2, n, 1):
    if n%i==0:
        flag = True
if not(flag):
    print("prime")
else:
    print("not prime")



#printing prime numbers upto:
#remember a can only start from 2:

a = int(input())
n = int(input())
for i in range(a, n+1, 1):
    flag = False
    for j in range(2,i,1):
        if i%j==0:
            flag = True
    if not(flag):
        print(i)