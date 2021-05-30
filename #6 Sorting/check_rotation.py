
def checkRotate(array):
    i=0
    count = 1
    while i < len(array):
        if array[i]<array[i+1]:
            count+=1
        else:
            print(count)
            break
        i+=1
    else:
        print(0)


N = int(input())
if N<=1:
    print()
else:
    arr = [int(x) for x in input().split()]
    checkRotate(arr)