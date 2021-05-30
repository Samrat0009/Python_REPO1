#______________________________________# insertion sort !!

# NOTE : unlike any sorting, here we just shift bigger element and place the smaller element before it !!
def insertSort(array):
    length = len(array)
    for i in range(1,length):
        j = i-1
        temp= arr[i]
        while (j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1]=temp
    for i in range(length):
        print(array[i],end=" ")



n = int(input())
if n<=1:
    print()
else:
    arr = [int(x) for x in input().split()]
    insertSort(arr)