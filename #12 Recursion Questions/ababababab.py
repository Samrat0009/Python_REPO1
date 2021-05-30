## Read input as specified in the question.
## Print output as specified in the question.
def baba(str,si,ei,x):
    if (si+3)>ei:
        return x
    if str[si]=='a' and str[si+1]=='b' and str[si+2]=='a':
        x = False
        return baba(str,si+1,ei,x)
    elif str[si]=='a' and str[si+1]=='b' and str[si+2]=='b' and str[si+3]=='b' :
        x = False
        return baba(str,si+1,ei,x)
    elif str[si]=='b' and str[si+1]=='b' and str[si+2]=='b' and str[si+3]=='b' :
        x = False
        return baba(str,si+1,ei,x)
    else:
        return baba(str,si+1,ei,x)

str = input()
l = int(len(str))

if baba(str,0,l-1,x=True):
    print("true")
else:
    print("false")