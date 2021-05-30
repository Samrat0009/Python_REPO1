def rep(str,si,ei):
    if si==(int(len(str))-1):
        return str
    if str[si] == str[si+1]:
        str = str[:si+1] + '*' + str[si+1:]
        return rep(str,si+1,ei)
    else:
        return rep(str,si+1,ei)


str = input()
print(rep(str,0,int(len(str))-1))