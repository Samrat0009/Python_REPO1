def checkPermutation(str1,str2):
    l = len(str1)
    count = 0
    for char in str1:
        for i in range(len(str2)):
            if char == str2[i]:
                count+=1
                str2 = str2.replace("str2[i]","5")
                break
    if count == l:
        return True
    else:
        return False

str1 = input()
str2 = input()
print(len(str1),len(str2))

if len(str1) == len(str2):
    checkPermutation(str1,str2)
    isPermutation = checkPermutation(str1, str2)
    if isPermutation:
        print("true")
    else:
        print("false")
else:
    print("false")