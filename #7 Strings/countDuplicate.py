def countDuplicate(string):
    newstr = ""
    string += ' '
    l = len(string)
    count = 1
    for i in range(l-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            print(string[i],end="")
            if count > 1:
                print(count, end="")
            count = 1
    print(string[-1])



#main
str = input()
if len(str) <= 1:
    print()
else:
    countDuplicate(str)