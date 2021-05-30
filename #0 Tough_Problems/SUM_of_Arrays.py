#________________________# summing unSorted arrays !!


# input: 3
#        6 2 4
#        3
#        7 5 6
# output:1 3 8 0

def sumArr(array1, array2):
    if N >= M:
        x = N
        j = 0
        while (j < (N - M)):
            array2.insert(j, 0)
            j += 1

    else:
        x = M
        i = 0
        while (i < (M - N)):
            array1.insert(i, 0)
            i += 1

    i = 1
    k = 1
    sum = []
    carry = 0
    while (k <= x):
        sum.append(((array1[-i] + array2[-i]) % 10 + carry) % 10)

        if (array1[-i] + array2[-i] + carry) > 9:
            carry = 1
        else:
            carry = 0

        i += 1
        k += 1
    if k == x + 1:
        sum.append(carry)
    for i in range(1, len(sum) + 1):
        print(sum[-i], end=" ")


N = int(input())
if N < 1:
    print()
else:
    arr1 = [int(x) for x in input().split()]

M = int(input())
if M < 1:
    print()
else:
    arr2 = [int(x) for x in input().split()]

arr = sumArr(arr1, arr2)