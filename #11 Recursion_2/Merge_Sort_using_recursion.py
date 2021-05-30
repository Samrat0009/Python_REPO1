def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid = len(arr)//2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    mergeSort(a1)                                   # will work because of PMI : induction hypothesis !!
    mergeSort(a2)

    return merge(a1,a2,arr)

def merge(a1,a2,arr):
    i=0
    j=0
    k=0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            k+=1
            i+=1
        else:
            arr[k] = a2[j]
            k+=1
            j+=1
    while i < len(a1):          # this is for bache hue elements in list!!
        arr[k] = a1[i]
        k += 1
        i += 1
    while j < len(a2):
        arr[k] = a2[j]
        k += 1
        j += 1




#n=int(input())
#arr=list(int(i) for i in input().split())
arr = [10,5,9,3,6,4,3]
mergeSort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")