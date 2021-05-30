n = int(input())
num = 64          # ASCII for 'A'
i=1
while(i<=n):
    j=0
    num = num + 1
    while(j<i):
        ch = chr(num)
        print(ch,end="")
        j = j+1
    print()
    i=i+1

