###                            FUNCTION IN FUNCTION  !!


def fact(n):
    n_fact = 1
    for i in range(1, n + 1, 1):
        n_fact = n_fact * i
    return n_fact


def ncr (n,r):
    n_fact = fact(n)
    r_fact = fact(r)
    n_r_fact = fact(n - r)
    ans = n_fact // (r_fact * n_r_fact)
    return ans                                                        ## here we 'return' ans !!!!


n = ncr(4,2)
print((n))