
N = int(input())
li = [int(a) for a in input().split()]
sum = 0
for i in range(0,len(li),1):
    sum = sum + int(li[i])

print(sum)