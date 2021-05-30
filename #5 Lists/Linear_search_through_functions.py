def linear_search(list,element):
    for i in range(len(list)):
        if list[i]==element:
            return i
            break
    else:
        return -1





li = [1,2,3,4,5]

index = linear_search(li,3)                   # using function linear search
print("index =",index)