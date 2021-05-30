#________________________________________________________# new list method !#_______________________________________________________________________________________#

# given a list : check if sorted :

#Base case : list of size 0 or 1 (is by default sorted!) : should return TRUE  (induction hypothesis)

# check if [0]>[1] : if yes return FAlSE (list not sorted)

# now to check list of size L-1: sorted or not

def isSorted(arr):
    l = len(arr)
    if l==0 or l==1:            # base case 1
        return True
    if arr[0]>arr[1]:           # base case 2
        return False

    # if NOT then : check base case 2 for : 1 till the end of list again, then, again then, again till true or list ends (restofList) !

    restofList = arr[1:]        # new list every time function is called !
    isSorted(restofList)
    # when all cases have passed through base case 2
    if isSorted(restofList):
        return True
    else:
        return False

a = (1,2,3,4,5,6,9,8)
print(isSorted(a))