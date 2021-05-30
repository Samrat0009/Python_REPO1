#__________________________________________# using split() for string conversion to list !

str = "my name is parikh"
li = str.split()                   # it will split wherever it finds a space  ' ' !!
print(li)

# output : ['my', 'name', 'is', 'parikh']

#                                 OR :

str = "my, name, is, parikh"
li = str.split(',')                   # it will split wherever it finds a comma (,) !!
print(li)

#___________________________________________# replace() function !!

str = "my name is parikh"
str.replace("parikh","rohan")                       # this will not do anything because strings are immutable
str = str.replace("parikh","rohan")                 # but
print(str)                                          # if you store it in a new string 'str' it will work !!

#___________________________________________# find() function !!

str1 = "my name is parikh parikh"
index = str1.find("par",16,21)                  # this means "my" is 16 (start) index and "parikh" is 21 (end) index !
print(index)

#__________________________________________#lower() and upper() functions !

str = "my name is rohan"
str = str.lower()
print(str)
str = str.upper()
print(str)

#__________________________________________# startswith() function !

str = "my name is rohan"
ans = str.startswith("my name")
print(ans)

#or:

str = "my name is rohan"
ans = str.startswith("par",11,25)
print(ans)