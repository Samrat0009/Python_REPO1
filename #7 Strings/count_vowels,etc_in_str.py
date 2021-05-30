def exploreString(str):
    vowel = 0
    for char in str:
        li = 'aeiouAEIOU'
        for i in range(len(li)):
            if char == li[i]:
                vowel+=1
    return vowel


str = 'alDFejfb7836A8D217nqql@@%^ eA#F'

str = exploreString(str)
print(str)