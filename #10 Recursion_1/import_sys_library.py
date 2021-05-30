import sys
sys.setrecursionlimit(3000)

def fact(n):
    if n == 0:
        return 1
    smallfact = fact(n-1)
    return n * smallfact

n = int(input())
print(fact(n))

#Note python max depth in this case is limited to 1000 so if you find the factorial of a number greater than 1000 it shows error!!

# to overcome that there is a library which needs to be imported!!

