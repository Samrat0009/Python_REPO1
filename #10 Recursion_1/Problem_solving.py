#_____________________________________________________________# Sum of 1st n natural numbers !_________________________________________________________________________

#concept : E(n) = n + E(n-1)  ______where n is the base case and rest is the follow.

def sum_n(n):
    if n == 0:
        return 0
    smalloutput = sum_n(n-1)
    return (n + smalloutput)

n = int(input())
print(sum_n(n))


# similarly !

def fact(n):
    if n == 0:
        return 1
    smallfact = fact(n-1)
    return n * smallfact

n = int(input())
print(fact(n))