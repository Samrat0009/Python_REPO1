#_____________________________# Array intersection !!


def unique_arr(list_1,list_2):
    i = 0
    while i<N1:
        count = 0
        j = 0
        while j<N2:
            if list_1[i] == list_2[j]:
                list_2[j] = 9999999999
                count = count + 1
                break
            j=j+1
        if count >= 1:
            print(list_1[i])
        i=i+1

N1 = int(input())
if N1<=1:
    print()
else:
    li1 = [int(x) for x in input().split()]

N2 = int(input())
if N2<=1:
    print()
else:
    li2 = [int(x) for x in input().split()]

unique_arr(li1,li2)