#_______________________________# Mutable !

x = 3
a = 3
print(x)

print(id(a))                    # this will be same                     because both are pointing at same reference
print(id(x))                    # as this


#__________________________________# Immutable !

li = [1,2,3,4]
li2 = li

print(li2)
print(li)

li[2] = 4

print(li2)                           # here both change because both were pointing to the same reference !!
print(li)                            # so modifying one of the lists will modify the other list too !!