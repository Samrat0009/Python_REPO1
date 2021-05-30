def power(x,n):
    if (n == 0):
        return 1
    elif (x == 0):
        return 0

    smalloutput = power(x,n-1)
    output = x*smalloutput
    return output

x,n = (int(k) for k in input().split())
print(power(x,n))