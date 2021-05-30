def fact(n):
    if n == 0:
        return 1
    smallfact = fact(n-1)
    return n * smallfact

n = int(input())
print(fact(n))