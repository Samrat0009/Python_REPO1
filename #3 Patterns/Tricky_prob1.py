#sample output:
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

n = int(input())
i=1
while(i<=n):
    p=1
    while(p<i):
        print(0,end="")
        p=p+1
    print('*',end="")
    p = n-i
    while (p > 0):
        print(0, end="")
        p = p - 1
    print('*',end="")
    p = n - i
    while (p > 0):
        print(0, end="")
        p = p - 1
    print('*',end="")
    p = 1
    while (p < i):
        print(0, end="")
        p = p + 1
    print()
    i=i+1
