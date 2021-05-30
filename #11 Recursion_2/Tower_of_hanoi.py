def towerofhanoi(n,a,b,c):
    if n==1:                            # base case
        print(a, c)
        return
    towerofhanoi(n-1,a,c,b)
    print(a, c)
    towerofhanoi(n-1,b,a,c)

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')