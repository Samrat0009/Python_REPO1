def remDuplicates(str):
    if len(str)==1:
        return str[0]
    if str[0]==str[1]:
        return remDuplicates(str[1:])
    else:
        return str[0] + remDuplicates(str[1:])

str = input()
print(remDuplicates(str))
