# *name = empty tuple !

# variable input :

def sum(a,b, *more):   # *more is used if you dont know how many variables will enter function !
    ans = a + b
    for i in more:
        ans = ans + i
    return ans

print(sum(2,3,4,5,6))


# variable output :

def operate(a,b):
    return a+b,a-b,a*b

d,e,f = operate(4,1)
print(d)                   # sum is stored in d
print(e)                   # diff is stored in e
print(f)                   # product in f