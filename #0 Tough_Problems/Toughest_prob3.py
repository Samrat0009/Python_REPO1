def spiralPrint(arr):
    spiral = []
    for i in range(n-1):
    # forward appending starting rows :
        for j in range(i,n-i-1):
            spiral.append(arr[i][j])
    # downward appending last columns :
        for j in range(i,m-i-1):
            spiral.append(arr[j][n-i-1])
    # backwards appending last rows :
        for j in range(n-i-1,i,-1):
            spiral.append(arr[m-i-1][j])
    # upward appending starting columns :
        for j in range(m-i-1,i,-1):
            spiral.append(arr[j][i])

    for i in range(len(l)):
        print(spiral[i],end=" ")

# Main
l = [int(i) for i in input().split()]
m, n = l[0], l[1]
if m<=1 and n<=1:
    arr = [[l[(j * n) + i + 2] for i in range(n)] for j in range(m)]
    print(arr[0][0])
else:
    arr = [[l[(j * n) + i + 2] for i in range(n)] for j in range(m)]
    spiralPrint(arr)