def sumofnum(str,k,l,x):
    if l==1:
        return str
    if k>l:
        return x
    if k<=l:
        x += int(str[k])
        return sumofnum(str,k+1,l,x)
    return x
str = input()
n = int(len(str))
print(sumofnum(str,0,n-1,0))