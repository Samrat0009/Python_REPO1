# NOTE : the array needs to be sorted !!!

# we donot copy this time but we use start index/ end index !!

def binarySearch(arr,x,si,ei):           # initially si = 0 and ei = len(str) !!!
    if si > ei:                        # base case
        return ' we didnt find it '
    mid =  (si + ei)//2
    if arr[mid] == x:
        return mid
    if arr[mid]>x:
        return binarySearch(arr,x,si,mid-1)            # every time this or
    else:
        return  binarySearch(arr,x,mid+1,ei)          # this happens: array gets shorter and we do not need extra steps !!
print(binarySearch([1,2,3,4,5,7,8,9,11,23,24,26,28],23,0,13))