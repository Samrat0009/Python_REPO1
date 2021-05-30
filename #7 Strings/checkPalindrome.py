## Read input as specified in the question.
## Print output as specified in the question.
def checkPalindrome(string):
    l = int(len(string) // 2)
    count = 0
    i = 0
    j = 1
    while i<=l and j<=(l+1 ):
        if string[i] == string[-j]:
            count += 1
        j+=1
        i+=1
    if count >= l:
        return True
    else:
        return False


str = input()
checkPalindrome(str)

isPalindrome = checkPalindrome(str)
if isPalindrome:
    print("true")
else:
    print("false")