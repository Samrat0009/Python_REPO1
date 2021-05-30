def removeX(str):
    if len(str)==0:
        return ' '
    if str[0]=='x':
        return removeX(str[1:])
    else:
        return str[0] + removeX(str[1:])

str = (input())
print(removeX(str))