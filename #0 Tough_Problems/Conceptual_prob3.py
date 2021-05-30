# Note :  Run Individually !!


#_________________________________# Pair Sum !!

def sum(list):
    i = 0
    while i<N:
        flag = False
        j = i+1
        while j<N:
            if list[i] + list[j] == x and i != j:
                if list[i] < list[j]:
                    print(list[i], list[j])
                else:
                    print(list[j], list[i])
            j=j+1
        i=i+1

N = int(input())
if N<=1:
    print()
else:
    li = [int(x) for x in input().split()]
    x = int(input())

sum(li)

#_________________________________# Triplet Sum !!

def sum(list):
    i = 0
    while i<N:
        j=i+1
        while j<N:
            k = j+1
            while k<N:
                if (list[i] + list[j] + list[k]) == x and i != j and i!=k and j!=k:
                    if list[i] <= list[j] and list[i] <= list[k]:
                        if list[j]<=list[k]:
                            print(list[i], list[j],list[k])
                        else:
                            print(list[i],list[k],list[j])
                    elif list[j] <= list[i] and list[j] <= list[k]:
                        if list[i]<=list[k]:
                            print(list[j], list[i],list[k])
                        else:
                            print(list[j],list[k],list[i])
                    else:
                        if list[i]<=list[j]:
                            print(list[k], list[i],list[j])
                        else:
                            print(list[k],list[j],list[i])
                k=k+1
            j=j+1
        i=i+1

N = int(input())
if N<=1:
    print()
else:
    li = [int(x) for x in input().split()]
    x = int(input())

sum(li)