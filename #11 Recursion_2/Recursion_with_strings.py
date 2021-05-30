# replace all occurrences of a with b for : example : str = "abdjabaubadb"

# NOTE : strings are immutable : that is u cannot change within the string so you have to create a string every time!!!

# base case = len(str) = 0 : do nothing

def replaceChar(str,a,b):
    if len(str) == 0:
        return str
    if str[0] == a:
        return b + replaceChar(str[1:],a,b)           # NOTE : calculation is done always after the function has been called till as many times it can be called !!
    else:                                             # means : b+b+b+replaechar(last time call hoga),then!!, saare add honge, aur ek complete string output milega!!
        return str[0] + replaceChar(str[1:],a,b)

print(replaceChar("ccbdghc",'c','x'))