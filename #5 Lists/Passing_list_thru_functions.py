def increment(li):
    li[0] = li[0] + 2
    return                                     # even when you don't return li

li = [1,2,3,4]                                             # or
increment(li)                                  # store it in any other list !
print(li)                                      # it still increases

#_____________________________# this is because the list, unlike variables, points to same reference even after a change !!



# another case :

def increment(li):
    # li[0] = li[0] + 2
    li = [3,2,3,4]                        # here this means a new list has been created
    return li                             # so when you return li without storing it like li = increment(li)

li = [1,2,3,4]                            # you get the same output as this 'li' list.
increment(li)
print(li)


# but if you want it changed this way :

def increment(li):
    # li[0] = li[0] + 2
    li = [3, 2, 3, 4]
    return li


li = [1, 2, 3, 4]
li = increment(li)                   # you have to store it first like this   !!!
print(li)                            # then your output will show a modified list !
                                     # which is actually a new list
