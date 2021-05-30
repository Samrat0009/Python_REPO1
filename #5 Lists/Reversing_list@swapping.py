#______________________________________________#  SWAPPING !!


def reverse(list):
    n = len(list)
    for i in range(0,n//2,1):
        li[n-i-1],list[i] = li[i],list[n-i-1]                    ##  this is the syntax

li = [1,2,3,4,5,6,7]
reverse(li)
print(li)

# output : [7, 6, 5, 4, 3, 2, 1]



#___________________________________________# swapping alternate !!

def reverse_alt(list):
    if x%2==0:
        n = len(list)
        for i in range(0,n,2):
            list[i+1],list[i] = list[i],list[i+1]                    ##  this is the syntax
        for i in range(n):
            print(li[i],end=" ")
    else:
        n = len(list)
        for i in range(0,n-1,2):
            list[i+1],list[i] = list[i],list[i+1]                    ##  this is the syntax
        for i in range(n):
            print(li[i],end=" ")


x = int(input())
if x==0:
    print()
else:
    li = [int(x) for x in input().split()]
    reverse_alt(li)
