def checkDuplicate(string):
    newstr = ""
    l = len(string)
    for i in range(l-1):
        if string[i] == string[i+1]:
            continue
        else:
            newstr += string[i]
    newstr += string[l-1]
    print(newstr)



#main
str = input()
if len(str) <= 1:
    print()
else:
    checkDuplicate(str)