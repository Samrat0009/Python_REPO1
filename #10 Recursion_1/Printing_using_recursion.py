# printing numbers from 1 to n :
# base case : 1 to n

def print1ton(n):
    if n==0:
        return
    smalloutput = print1ton(n-1)
    print(n,end=" ")
    return

n = int(input())
print1ton(n)

print()

#__________________ for reverse :

def revprint1ton(n):
    if n==0:
        return
    print(n,end=" ")
    smalloutput = revprint1ton(n-1)
    return

n = int(input())
revprint1ton(n)