def staircase(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase(n - 3) + staircase(n - 2) + staircase(n - 1)
    
n = int(input())
print(staircase(n))

#             or

def countWays(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]

n = int(input())
print(countWays(n))

