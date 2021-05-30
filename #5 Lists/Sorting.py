#_________________________________________________# Sorting !!

def sort(list):
    i = 0
    count = 0
    li = []
    while i<N:
        if list[i] == 0:
            li.insert(count,0)
            count = count + 1
        i=i+1
    j = 0
    while j<N:
        if list[j] == 1:
            li.insert(count,1)
            count = count + 1
        j=j+1
    print(li)

N = int(input())
if N<=1:
    print()
else:
    li = [int(x) for x in input().split()]
    sort(li)
