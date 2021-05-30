## JUST RUN THE SI BACKWARDS : DUH !!

#import
from sys import setrecursionlimit
setrecursionlimit(11000)

def firstIndex(arr, x, si):
    l = len(arr)
    if si == 0:
        return -1
    if arr[l-1]==x:
        return l-1
    if arr[si]==x:
        return si
    return firstIndex(arr,x,si-1)


# Main
n=int(input())
arr=list(int(i) for i in input().split())
x=int(input())
l = len(arr)
print(firstIndex(arr, x, l-1))
