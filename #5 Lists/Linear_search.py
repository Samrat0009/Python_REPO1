n = int(input())                # no of elements

li = [int(x) for x in input().split()]            # elements in the list

print(li)


ele = int(input())        # element to be searched

isFound = False
for i in range(len(li)):                # searches elements in the list
    if li[i] == ele:
        print(i)
        isFound = True
        break
if isFound is False:
    print(-1)

