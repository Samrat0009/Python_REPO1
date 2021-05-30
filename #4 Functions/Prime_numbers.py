def isPrime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            break
    else:
        return True
    return False

###   PRINTING PRIME NUMBERS !!!!


####            1. short way !!!!

def print_Prime(a,n):
    for i in range (a,n+1,1):
        is_i_prime = isPrime(i)
        if is_i_prime:
            print(i)

a = int(input())
n = int(input())
print_Prime(a,n)

####           2.  long way !!!!

def print_prime(a,n):
    for i in range(a,n+1,1):
        flag = False
        for j in range(2,i,1):
            if i%j==0:
                flag = True
        if not(flag):
            print(i)

a = int(input())
n = int(input())
print_prime(a,n)


