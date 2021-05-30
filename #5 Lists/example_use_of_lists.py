#_______________________________________# find unique in list !!


def unique(list):
    i = 0
    while i<N:
        count = 0
        j = 0
        while j<N:
            if list[i] == list[j]:
                count = count + 1
            j=j+1
        if count == 1:
            print(li[i])
            break
        i=i+1

N = int(input())
if N<=1:
    print()
else:
    li = [int(x) for x in input().split()]
    unique(li)
