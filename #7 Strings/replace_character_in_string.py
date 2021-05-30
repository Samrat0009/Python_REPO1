def replace(str,char1,char2):
    newstr = ""
    for char in str:
        if(char==char1):
            newstr += char2
        else:
            newstr += char
    return newstr

str = 'fdslkjssggs'
str = replace(str,'s','d')
print(str)