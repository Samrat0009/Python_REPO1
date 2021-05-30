##awesome code
def F(n):
    k = 1
    i = 1
    r = 1                              # n=1 and n=2 pe it will print 1 bcoz r=1 by default
    count = 3
    while (count <= n):                ## and for n>=3 it will call any fibonacci no, you want!!!
        r = i + k
        i = k
        k = r
        count = count + 1
    if n == 0:
        print(0)                        # n=0 pe it will print 0
    else:
        print(r)


n = int(input())
F(n)
