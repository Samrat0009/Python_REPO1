def largestRowCol(arr):
    rowsum = 0
    rowhigh = 0
    count = -1
    for subarr in arr:
        high1 = 0
        count += 1
        for ele in subarr:
            high1 += ele
            if high1 >= rowsum:
                rowhigh = count
                rowsum = high1

    colsum = 0
    colhigh = 0
    for i in range(n):
        high2 = 0
        for j in range(m):
            high2 += arr[j][i]
        if high2 >= colsum:
            colhigh = i
            colsum = high2
    if rowsum >= colsum:
        print(end="row ")
        print(rowhigh,rowsum)
    else:
        print(end="column ")
        print(colhigh,colsum)


#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
largestRowCol(arr)