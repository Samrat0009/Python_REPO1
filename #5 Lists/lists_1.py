#__________________________________________________________# syntax :

li = [1,2,"parikh",3,4]

print(li)

#__________________________________________________________# modifying list :

li[0] = 5

print(li)

#_________________________________________________________# slicing list :


print(li[1:3])                 # shows elements from index '1' to index (3-1)  '2'

print(li[0:3])                 # shows elements from index '0' to index (3-1)  '2'

print(li[1:])                 # shows elements from index '1' to last

#______________________________________________________# adding elements :

li.insert(1,7)                  # syntax : li.insert(index,element)

li.insert(4,"hello")

print(li)

#________________________________________________________# adding multiple elements :

li.extend([9,10,11])

print(li)

#________________________________________________________# removing elements :

li.remove(5)                     # here   5 is the not the index   but value

print(li)                        # this will remove the value '5'

# so to remove by index :


li.pop(2)                        # pops out /removes 2nd index

print(li)

