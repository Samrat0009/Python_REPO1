n = int(input())
i=1
num = 65
while(i<=n):
    j=1
    num = 65 + n - i
    while(j<=i):
        ch = chr(num)
        print(ch,end="")
        j=j+1
        num = num+1
    print()
    i=i+1
5