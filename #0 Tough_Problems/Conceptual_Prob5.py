from sys import setrecursionlimit
setrecursionlimit(11000)

def checkNumber(arr, x):
    l = len(arr)
    if l==0:                                 # when length of array becomes 0 after recursively calling it : return false (to avoid list index out of range)
        return False
    if arr[0] == x:                            # base case 1
        return True
    elif arr[0] != x:
        restofarray = arr[1:]
        return checkNumber(restofarray,x)               # NOTE : when calling a function recursively it has to be returned : "return" checkNum.....




# Main
n=int(input())
arr=list(int(i) for i in input().split())
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
