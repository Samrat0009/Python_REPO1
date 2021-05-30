def Rotate(array):
    i = 0
    arr = []
    while i < N - d:
        arr.append(array[i + d])
        i += 1
    i = 0
    while i < d :
        arr.append(array[i])
        i += 1

    for i in range(len(arr)):
        print(arr[i], end=" ")

N = int(input())
if N <= 1:
    print()
else:
    arr = [int(x) for x in input().split()]
    d = int(input())

Rotate(arr)