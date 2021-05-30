# much better than bubble,insertion,selection sort, arguably faster than merge sort !!

# logic : take first case (say no.3) take it to index=3 , now make sure all number smaller than 3 are before 3 and rest after 3 using "swap"!
#       : now quick sort both sides again and again till completely sorted !!

# quick sort : QS,SI,EI

# base case : if SI >= EI : return (len = 0/1 no sorting required)

import sys
sys.setrecursionlimit(5000)

def quickSort(arr,si,ei):
    if si >= ei:                                                #array is empty 1        # base case
        return

    count=0
    for i in range(len(arr)):
        if arr[i]<= arr[si]:
            count+=1
    arr[si],arr[count-1] = arr[count-1],arr[si]
    p = count

    if arr[si] >= arr[ei-1]:
        if si >= ei:  # array is empty 1        # base case
            return
        else:
            arr[si],arr[ei-1] = arr[ei-1],arr[si]
        si+=1
        ei-=1
                                                                        #partition(arr,a1,a2)
    quickSort(arr,si,p-1)
    quickSort(arr,p+1,ei)

    return


n=int(input())
arr=list(int(i) for i in input().split())
quickSort(arr, 0, n)
for i in range(len(arr)):
    print(arr[i],end=" ")