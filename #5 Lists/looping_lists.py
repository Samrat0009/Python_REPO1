li = [1,2,"Parikh",9,10,11,"Ankush"]
print(li)


#_____________________________________________# running loop using range !!
for i in range(len(li)):
    print(li[i])



#_____________________________________________# direct way to run list !!

for ele in li:
    print(ele)


for ele in li[2:]:                         # run list from 2 to end
    print(ele)

for ele in li[2:5]:                        # run list from 2 to 4
    print(ele)


for ele in li[2]:                          # prints reference of data in index = 2 line by line
    print(ele)                             # output :
                                            # p
                                            # a
                                            # r
                                            # i
                                            # k
                                            # h