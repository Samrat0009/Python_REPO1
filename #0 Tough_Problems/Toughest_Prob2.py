#sample input : 8
#sample output :

#1 2 3 4 5 6 7 8
#17 18 19 20 21 22 23 24
#33 34 35 36 37 38 39 40
#49 50 51 52 53 54 55 56
#57 58 59 60 61 62 63 64
#41 42 43 44 45 46 47 48
#25 26 27 28 29 30 31 32
#9 10 11 12 13 14 15 16



n = int(input())
if n%2==0:
    p=int(n/2)
else:
    p=int((n+1)/2)


if n%2!=0:
    i=1
    while i <=n:
        print(i,end=" ")
        i=i+1
    print()

    j=1
    while j<p:
        k=1
        s = n*2*j
        while s+k<=(n+s):
            print(s+k,end=" ")
            k=k+1
        print()
        j=j+1

    j=p+1
    while j<n:
        k=n+1
        s = n*2*(n-j)
        while s+k<=(s+2*n):
            print(s+k,end=" ")
            k=k+1
        print()
        j=j+1

    i = n+1
    while i <= 2*n:
        print(i, end=" ")
        i = i + 1
    print()

else:
        i = 1
        while i <= n:
            print(i, end=" ")
            i = i + 1
        print()

        j = 1
        while j < p:
            k = 1
            s = n * 2 * j
            while s + k <= (n + s):
                print(s + k, end=" ")
                k = k + 1
            print()
            j = j + 1

        j = p + 1
        while j < n:
            k = n + 1
            s = n * 2 * (n - j)
            while s + k <= (s + 2 * n):
                print(s + k, end=" ")
                k = k + 1
            print()
            j = j + 1

        i = n + 1
        while i <= 2 * n:
            print(i, end=" ")
            i = i + 1
        print()