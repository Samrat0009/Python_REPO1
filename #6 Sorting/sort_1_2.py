
def sort(array):
    i=0
    while i < 3:
        low = i
        j=0
        while j< len(array):
            if array[j] == low:
                print(low,end=" ")
            j+=1
        i+=1

N = int(input())
if N<=1:
    print()
else:
    arr = [int(x) for x in input().split()]
    sort(arr)