# logic : select the minimum element in array and put it first !

def selectionSort(arr):
    length = len(arr)
    # put the correct element at ith position
    for i in range(length-1):
        minIndex=i
        # index of minimum element for this iteration
        for j in range(i+1,length):
            if arr[j]<arr[minIndex]:
                minIndex = j
                arr[i],arr[minIndex] = arr[minIndex],arr[i]


arr = [3,2,6,4,5,1]
selectionSort(arr)
print(arr)