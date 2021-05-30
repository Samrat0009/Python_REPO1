def checkPalindrome(num):
    v = 0
    isPalindrome = num
    while (num > 0):
        rem = num % 10
        div = int(num / 10)
        num = div
        v = v * 10 + rem
    if (isPalindrome == v):
        print('true')
    else:
        print('false')


num = int(input())
result = checkPalindrome(num)
