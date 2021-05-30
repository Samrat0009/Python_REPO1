def wavePrint(arr):
        for i in range(n):
            if i%2==0:
                for j in range(m):
                    print(arr[j][i],end=" ")
            else:
                for j in range(m-1,-1,-1):
                    print(arr[j][i],end=" ")


#Main
l=[int(i) for i in input().split()]
m, n = l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
wavePrint(arr)

# input : 3 4 1  2  3  4 5  6  7  8 9 10 11 12
# output : 1 5 9 10 6 2 3 7 11 12 8 4