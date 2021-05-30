# multiple of 3

a = int(input())
b = int(input())

for i in range(a, b+1, 1):
    if i%3==0:
        print(i)

# but this loop runs 10 times!


#2nd method:

a = int(input())
b = int(input())

if a%3==0:
    s=a
if a % 3 == 1:
    s = a+2
else:
    s = a+1

for i in range(s, b+1, 3):
    print(i)


# here we write more code but the code runs less number of times
