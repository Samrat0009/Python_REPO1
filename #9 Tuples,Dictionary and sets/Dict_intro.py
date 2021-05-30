# example : used to count words in a sentence in a faster way !

# ways of creating a dictionary !

dict = {}
print(type(dict))

dict = {"the":1,"a":5,3:4}
print(dict)
print(len(dict))

# copying dictionary :`
b = dict.copy()
print(b)

#_____another way of creating dictionary :

#c = dict.fromkeys([["the",32,5,"a"],10])
#print(c)


#____another way :

c = dict([("the",3),("a",10),(3,4)])
print(c)
