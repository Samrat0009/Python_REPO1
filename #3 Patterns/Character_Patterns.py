 # Alphabets are represented by their ascii values

 ###                 NOTE:
 #  ord('alphabet') represents their ascii values
 #  chr('number') gives you the alphabet corresponding to this value




 # Printing the kth character in the alphabet:

k = int(input())                             # 'A' + k-1
x = ord('A')                                 #say 65
asciiTarget = x + k - 1                      # say k=4  then 65+4-1 = 68, so chr(68) = 'D'   so it will give you 'D'
targetChar = chr(asciiTarget)
print(targetChar)


# printing alphabets in square pattern

n = int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        charP = chr(ord('A') + j - 1)
        print(charP,end="")
        j=j+1
    print()
    i=i+1
