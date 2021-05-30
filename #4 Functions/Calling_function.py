# SCOPE OF VARIABLES !!

a1 = 10                ## global Variable


def f1():
    b1 = 12              ## local variable
    print(b1)


print (a1)

# print(b1)          :       This will give an error because it is not a global variable!!  this means that this function lies within a function
                            # so this can only be accessable inside the function it is defined in.
f1()

# NOTE :  you can call a  global variable inside a function as a local variable.

#########################         BUT :

##         CASE  1.

a4 = 13
def f4():
    a4 = 12                        ## python assumes you want to create a new local variable  a4
    print(a4)
    print(id(a4))

print(a4)
f4()
print(a4)
print(id(a4))

##       CASE   2.           (global)
a4 = 13
def f4():
    global a4                     ## this tells python to change the value of global variable a4 itself.
    a4 = 12
    print(a4)
    print(id(a4))

print(a4)
f4()
print(a4)
print(id(a4))