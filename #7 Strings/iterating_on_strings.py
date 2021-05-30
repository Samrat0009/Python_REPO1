#_________________________________________# 'in' Method:

str = 'hello world'

count = 0
for i in str:
    if i == 'l':
        count+=1
print(count)

#     OR

#_____________________________________# index-range Method !!

count = 0
for i in range(len(str)):
    if str[i] == 'l':
        count+=1
print(count)

#______________________________________________# 'in' and 'not in' : it checks whether a substring exists or not! #__________________________________________________________________________

str = 'hello'

if 'hel' in str:
    print('substring')

if 'heo' not in str:
    print('not a substring')