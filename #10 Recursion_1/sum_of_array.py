#import
from sys import setrecursionlimit
setrecursionlimit(11000)

def sumArray(arr):
    l = len(arr)
    if l==1:                          # base case 1
        return arr[0]
    restofarray = arr[1:]
    sum =  arr[0] + sumArray(restofarray)      #calling function
    return sum


#main
n=int(input())
arr=list(int(i) for i in input().split())
print(sumArray(arr))
