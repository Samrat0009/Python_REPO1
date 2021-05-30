# "ab".join([1,2,3]) : 1ab2ab3ab
# "ab".join("abc") : aabbabcab

ab = "ab".join("abcd")
print(ab)

# similarly we can join lists :

ab = "ab".join(["1","2","3","4"])                # NOTE :  it stops at n-1 !!
print(ab)

#alternative to join ab to 4 too !!

ab = "ab".join(["1","2","3","4",""])
print(ab)

#____________________________________________________# IMPORTANT example :


li = [[1,2,3,4],[5,6],[9,10,11,12]]
n=3
for row in li:
    output = ' '.join(str(ele) for ele in row)
    print(output)