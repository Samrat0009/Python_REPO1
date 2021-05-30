# Two main concepts in OOPS:
# 1. classes
# 2. Objects

# way to create a class : and a function inside it :

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = student("abc",16)

s2 = student("def",17)

# display s1 and s2 address:

print(s1,s2)

# print type of anything (obj,class,list,string)

print(type(s1))

#print all info about

print(s1.__dict__)

# check if object has attribute:

print(hasattr(s1,"name"))       # checks if s1 has name attribute.

#display the attribute:

print(getattr(s1,"name"))

#delete the attribute you want to remove

delattr(s2,"name")
print(s2.__dict__)