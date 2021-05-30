n = int(input())

for i in range(1,n+1,1):
    for j in range(1, i, 1):
        print(' ',end="")
    for l in range(i, n+1, 1):
        print(l,end="")
    print()
for i in range(1,n,1):
    for j in range(n-i, 1, -1):
        print(' ',end="")
    for l in range(n-i, n+1, 1):
        print(l,end="")
    print()
