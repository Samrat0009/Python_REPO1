
def zeroSort(array):
    i=0
    count=0
    arr = []
    while i < len(array):
        if array[i]!= 0:
            count+=1
            arr.append(array[i])
        i+=1

    while count < len(array):
        arr.append(0)
        count+=1

    for i in range(len(arr)):
        print(arr[i],end=" ")



N = int(input())
if N<=1:
    print()
else:
    arr = [int(x) for x in input().split()]
    zeroSort(arr)