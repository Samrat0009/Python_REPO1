#_______________________________________________________________#square of elements :
li = [1,2,3,4]
#_____________________________# long way :

li_new=[]
for ele in li:
    li_new.append(ele**2)
print(li_new)

#_______________________________________________________________# using comprehension now :

li_new_c=[ele**2 for ele in li]
print(li_new_c)

#___________________________________________________________# printing square of even elements only :

li_even_c=[ele**2 for ele in li if ele%2==0]
print(li_even_c)

# basically long 5-6 line codes have been reduced to a single line !!

#_______________________________________________________# multiple conditions : ex multiple of 6 :

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
li_6=[ele for ele in li if ele%2==0 and ele%3==0]                    # any number of conditions allowed !!
print(li_6)

#________________________________________________________________# multiple FOR LOOPS :

li1 = [1,2,3,4,5,6]
li2 = [2,4,6,7]
li_inter = []

for ele in li2:
    for ele1 in li1:
        if ele==ele1:
            li_inter.append(ele)
print(li_inter)

# OR :

li_inter_c = [ele for ele in li1 for ele1 in li2 if ele==ele1]
print(li_inter_c)

#____________________________________________________# ex: if multiple of 2 give square else print same element :

li = [1,2,3,4,5,6]
li_new = [ele**2 if ele%2==0 else ele for ele in li]
print(li_new)
