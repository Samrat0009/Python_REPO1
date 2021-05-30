li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]                  # considering we want a 3x4 array :
x=3
y=4

#____________________________________________#original way of printing :

for i in range(x):
    for j in range(y):
        print(li[i][j],end=' ')
    print()                                      # for changing column !
print()
# OR :

#________________________________________# here we do not need to know x and y !!!!!!!!!

li = [[1,2,3,4],[5,6],[9,10,11,12]]
for row in li:
    for ele in row:
        print(ele,end =' ')
    print()
print()
#_______________________________________________# using join() function :

li = [[1,2,3,4],[5,6],[9,10,11,12]]
n=3
for row in li:
    output = ' '.join(str(ele) for ele in row)
    print(output)