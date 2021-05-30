def rowWiseSum(arr):
    arr = [[ li[j*n+i] for i in range(n)] for j in range(m)]
    for ele in arr:
        sum1 = 0
        for i in ele:
            sum1 += i
        print(sum1,end=" ")
    print()
#Main
m, n=(int(i) for i in input().strip().split(' '))
li=[int(i) for i in input().strip().split(' ')]
rowWiseSum(li)
