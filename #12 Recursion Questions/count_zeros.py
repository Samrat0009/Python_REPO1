def zero(str,si,ei,count):
    if si>ei:
        return count
    if int(str[si])==0:
        return zero(str,si+1,ei,count+1)
    else:
        return zero(str,si+1,ei,count)

str = input()

for i in range(int(len(str))):
    if int(str[0])==0:
        str = str[1:]


print(zero(str,0,int(len(str))-1,0))