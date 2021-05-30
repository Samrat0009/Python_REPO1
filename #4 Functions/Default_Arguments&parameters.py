def f1(a,b,c=2,d=0):
    return a+b+c+d
print(f1(2,3,4,5))
print(f1(2,3))              ## by default c = 2 and  d=0     !!!!!
print(f1(2,3,4))            ## by default d = 0 !!!



# way to skip 'c' :

def f1(a,b,c=2,d=0):
    return a+b+c+d
print(f1(2,3,d=4))            ## by default c = 2,  and d takes 4 !!!
print(f1(2,3,4))              ## but here by default d = 0 !!!

