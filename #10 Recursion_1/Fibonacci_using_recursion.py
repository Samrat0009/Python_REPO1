# logic : fib(N) = fib(N-1) + fib(N-2)!

# base case = fib(1) = 1

def fib(n):
    if n==1 or n==2:
        return 1
                                #_______________# here we need multiple base cases
    fibo1 = fib(n-1)
    fibo2 = fib(n-2)
    output = fibo1 + fibo2
    return output

n = int(input())
print(fib(n))