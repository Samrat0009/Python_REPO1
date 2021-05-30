#import
from sys import setrecursionlimit
setrecursionlimit(11000)

def firstIndex(arr, x, si):
    l = len(arr)
    if si == l-1:
        return -1
    if arr[0]==x:
        return 0
    if arr[si]==x:
        return si
    return firstIndex(arr,x,si+1)


# Main
n=int(input())
arr=list(int(i) for i in input().split())
x=int(input())
print(firstIndex(arr, x, 0))
