# input : 7
# sample output:
#   7777777777777
#   7666666666667
#   7655555555567
#   7654444444567
#   7654333334567
#   7654322234567
#   7654321234567
#   7654322234567
#   7654333334567
#   7654444444567
#   7655555555567
#   7666666666667
#   7777777777777

n=int(input())

for i in range(0,n,1):
    k=n
    for j in range(0,n,1):
        if k>=n-i:
            print(k,end="")
        else:
            print(n-i,end="")
        k=k-1
    p=n-i+1
    k=1
    for j in range(1,n,1):
        if k<n-i:
            print(n-i,end="")
        else:
            print(p,end="")
            p = p + 1
        k=k+1
    print()

for i in range(n-2,-1,-1):                    ## manipulated for loop to start from behind!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    k=n
    for j in range(0,n,1):
        if k>=n-i:
            print(k,end="")
        else:
            print(n-i,end="")
        k=k-1
    p=n-i+1
    k=1
    for j in range(1,n,1):
        if k<n-i:
            print(n-i,end="")
        else:
            print(p,end="")
            p = p + 1
        k=k+1
    print()
