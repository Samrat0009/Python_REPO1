
def reverse(n):
    v=0
    while(n>0):
        rem = n%10
        div = int(n/10)
        n=div
        v=v*10+rem
    print(v)

n=int(input())
result = reverse(n)