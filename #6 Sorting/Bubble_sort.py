#________________________# Bubble Sort !!

# NOTE : unlike selection sort, in bubble sort we only swap two elements at a time !!

def bubbleSort(array):
    i=0
    while i < len(array):
        j=0
        while j < len(array)-1:
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
            j+=1
        i += 1
    for i in range(len(array)):
        print(array[i],end=" ")



N = int(input())
if N<=1:
    print()
else:
    arr = [int(x) for x in input().split()]
    bubbleSort(arr)