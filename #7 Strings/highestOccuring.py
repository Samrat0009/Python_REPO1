def highest(string):
    l = len(string)
    high =0
    for char in string:
        count = 0
        for i in range(l):
            if char == string[i]:
                count+=1
            if count > high:
                high = count
                chr = string[i]
    print(chr)

#main
str = input()
if len(str) <= 1:
    print()
else:
    highest(str)