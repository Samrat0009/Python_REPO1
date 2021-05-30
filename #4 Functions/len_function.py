## Read input as specified in the question.
## Print output as specified in the question.
def isArmstrong(num):
    length = len(str(num))                     ##   'len' function is used to calculate length of strings and arrays !!
    sum = 0
    temp = num
    while (temp != 0):
        rem = temp % 10
        sum = sum + ((rem) ** length)
        temp = temp // 10

    if sum == num:
        return True
    else:
        return False


num = int(input())

checkArmstrong = isArmstrong(num)
if checkArmstrong:
    print("true")
else:
    print("false")
