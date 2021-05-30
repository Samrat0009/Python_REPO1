# loops : work

a = 1,2,3,4,5
for i in a:
    print(i,end=" ")

# conditions : work

print()
if 7 in a:
    print(True)
else:
    print(False)
print(len(a))

# math : work

b = 6,7
c = a + b             # appends all elements of a and b together !!
print(c)
print(min(c))
c = (a,b)              # min and max (only comparable entries (int w/d int, float w/d float, etc !!!)
print(c)

# concat : repetition : works

e = b*4
print(e)

#list to tuple :
l = [1,2,3,4,5]
print(type(l))
l = tuple(l)
print(type(l))