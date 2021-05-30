# simplest for loop:

s = "abcd"
for c in s:
    print(c)

#output:
# a
# b
# c
# d

# printing numbers from 0 to n
#                                                   RANGE METHOD


n = int(input())
for i in range(0,n+1,2):                     ##  it will stop at n !!
    print(i)

#output:
# 0
# 2
# 4
# 6
# 8
# 10
