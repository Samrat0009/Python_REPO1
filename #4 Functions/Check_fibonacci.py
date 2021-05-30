
def checkMember(n):
    a=0
    b=1
    for i in range(0,n,1):
        k = a + b
        a = b
        b = k
        if n == k:
            break
    else:
        return False
    return True


n=int(input())

if(checkMember(n)):
    print("true")
else:
    print("false")