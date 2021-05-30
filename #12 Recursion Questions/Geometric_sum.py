def geosum(n,k,x):
    if k==0:
        return 1
    if n>k:
        return x
    x += 1/(2**n)
    return geosum(n+1,k,x)

k = int(input())
a=geosum(0,k,0)
print("{:.5f}".format(round(a, 5)))    # here 5 is the no of places to round up to &
                                       #  :5f if the number of decimals to be displayed
