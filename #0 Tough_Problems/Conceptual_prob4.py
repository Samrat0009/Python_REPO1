## Read input as specified in the question.
## Print output as specified in the question.



#_________________________# using function max(list) !!


def secondHigh(array):
    k = array[0]
    count = 0
    for j in range(len(array)):
        if array[j]==k:
            count+=1
    if count == len(array):
        print((-2)**31)
    else:
        i = 0
        high = max(array)
        print(high)
        for i in range(len(array)):
            if array[i] == high:
                array[i] = 0


        high2 = max(array)
        print(high2)


N = int(input())
if N<=1:
    print((-2)**31)
else:
    arr = [int(x) for x in input().split()]
    secondHigh(arr)