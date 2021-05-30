
#chooose an option for sum diff product etc
i=0
while (i<=5):
    n = int(input())
    if n==1:
        x = int(input())
        y = int(input())
        z = x + y
        print(z)
    elif n==2:
        x = int(input())
        y = int(input())
        z = x - y
        print(z)
    elif n==3:
        x = int(input())
        y = int(input())
        z = x * y
        print(z)
    elif n==4:
        x = int(input())
        y = int(input())
        z = x / y
        print(z)
    elif n==5:
        x = int(input())
        y = int(input())
        z = x % y
        print(z)
    elif n==6:
        exit(0)
    else:
        print("Invalid Operation")
    i = i + 1