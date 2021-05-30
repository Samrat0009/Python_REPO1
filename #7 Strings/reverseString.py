def reverse(string):
    newstr = ""
    l = len(string)
    for i in range(1,l+1):
        newstr += string[-i]

    li = newstr.split()
    for i in range(1,len(li)+1):
        print(li[-i],end=" ")



#main
str = input()
if len(str) <= 1:
    print()
else:
    reverse(str)