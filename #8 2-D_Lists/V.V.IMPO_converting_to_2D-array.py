li = [1,2,3,4,5,6,7,8,9,10,11,12]                  # considering we want a 3x4 array :

#______________# to do that we formulate : [i,j] = int(m*i + j) , ex :   [2,3] = 4*2 + 3 = 11

str = input().split()
x,y = int(str[0]),int(str[1])
b = [int(i) for i in input().split()]

arr = [[ b[y*i+j] for j in range(y)] for i in range(x)]

print(arr)

# input : 3 4
#         1 2 3 4 5 6 7 8 9 10 11 12
# output: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

#_________________# if we want all input in 1 single line


str = input().split()
x,y = int(str[0]),int(str[1])
b = str[2:]

arr = [[ int(b[y*i+j]) for j in range(y)] for i in range(x)]

print(arr)

# input : 3 4 1 2 3 4 5 6 7 8 9 10 11 12
# output : [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]