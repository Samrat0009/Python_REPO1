# generally fo 1D list we use : li = [int(x) for x in input().split()]

#_____________________# for list of list/ 2D list :

str = input().split()
x,y = int(str[0]),int(str[1])
li = [[int(j) for j in input().split()] for i in range(x)] # to take input lists for x no. of lines !!

print(li)

#________________________# jagged list :

n = int(input())
li = [[int(j) for j in input().split()] for i in range(n)] # to take input lists for n no. of lines !!

print(li)