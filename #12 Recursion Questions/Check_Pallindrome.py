def isPallindrome(st, s, e):
    if s == e:
        return True

    if st[s] != st[e]:
        return False

    if s < e + 1:
        return isPallindrome(st, s + 1, e - 1)

    return True

str = input()
l = int(len(str))
if isPallindrome(str,0,l-1):
    print("true")
else:
    print("false")