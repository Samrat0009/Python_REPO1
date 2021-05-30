#_____________________________________________________# introduction:

li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(li[2][3])

#_________________________________________________# storing data in 2D lists :

li = [[1,2,3,4],[5,6,7,8]]

print(li[0])

type(li[0])

li[0][1] = 4

print(li[0])

print(id(li))
print(id(li[0]))
print(id(li[1]))

#_________________________________________________# list of different types : not a 2D list :

li[1] = 'parikh'                      # this is no more a 2D list now !!!

print(li)