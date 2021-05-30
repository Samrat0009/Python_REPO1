# general ways of concatenation :

a = 'red'
print(id(a))
a = a + 'blue'
print(id(a))                    # new different string !

print(a)
print(a + 'green')              # same string !
print(id(a))
a+='red'
print(a)                        # new different string !
print(id(a))
# ,etc.....

a=a*3
print(a)
print(id(a))                   # new different string !

# NOTE :


# s  = 'red' + 3                : ERROR : concat of int and string not allowed in python !

s = 'red' + '3'
s1 = 'red' + str(3)              # only these two ways allowed !
print(s)
print(s1)
