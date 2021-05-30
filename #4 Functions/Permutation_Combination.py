#n = int(input())
#r = int(input())


#n_fact = 1
#for i in range(1,n+1,1):
#    n_fact = n_fact * i

#r_fact = 1
#for i in range(1,r+1,1):
#    r_fact = r_fact * i

#n_r_fact = 1
#for i in range(1,n-r+1,1):
#    n_r_fact = n_r_fact * i

#ans = n_fact//(r_fact*n_r_fact)
#print(ans)


##     In the form of a function:

def fact(n):
    n_fact = 1
    for i in range(1, n + 1, 1):
        n_fact = n_fact * i
    return n_fact

n = int(input())
r = int(input())

n_fact = fact(n)
r_fact = fact(r)
n_r_fact = fact(n-r)

ans = n_fact//(r_fact*n_r_fact)
print(ans)                                                          ## here we 'print' ans !!!!




###                            function in function  !!


def ncr (n,r):
    n_fact = fact(n)
    r_fact = fact(r)
    n_r_fact = fact(n - r)
    ans = n_fact // (r_fact * n_r_fact)
    return ans                                                        ## here we 'return' ans !!!!


ncr(5,2)