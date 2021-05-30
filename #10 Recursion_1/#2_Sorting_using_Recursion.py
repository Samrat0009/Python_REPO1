#____________________________________________________# start index method !#________________________________________________________________________________________#

# Other way of sorting : without making too many new lists !!

# 1. compare 0 and 1st element

# 2. the function is getting a new list and a new index every time : list, si(start index)

# if si = l-1 : base case : ( because list is sorted if only 1 element left)

# basically comparing si and si+1  : if in order :true, else : false

def isSorted2(arr,si):
    l = len(arr)
    if si == l-1 or si == l :    #i.e only 1 element left (l-1)   or list is emptied (l)
        return True
    if a[si]>a[si+1]:
        return False
    return isSorted2(arr,si+1)

a = (1,2,3,4,5,6,8,7)
print(isSorted2(a,0))             # a,0 because start index ko by default we put 0 !!