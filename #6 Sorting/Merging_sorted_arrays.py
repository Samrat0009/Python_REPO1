#________________________# Merging Sorted arrays !!


def mergeArr(array1,array2):
    i=0
    j=0

    arr = []

    while((i<N) and (j<M)):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i = i+1
        else:
            arr.append(arr2[j])
            j=j+1
    while i < N:
        arr.append(arr1[i])
        i = i + 1
    while j< M:
        arr.append(arr2[j])
        j = j+1
    for i in range(len(arr)):
        print(arr[i],end=" ")






N = int(input())
if N<1:
    print()
else:
    arr1 = [int(x) for x in input().split()]

M = int(input())
if M<1:
    print()
else:
    arr2 = [int(x) for x in input().split()]

arr = mergeArr(arr1,arr2)