#____________________________________________________# ex: if multiple of 2 give square else print same element :

li = [1,2,3,4,5,6]
li_new = [ele**2 if ele%2==0 else ele for ele in li]
print(li_new)

#____________________________________________________# ex2 : for loop condition for strings :

s = "parikh"

li = [ele for ele in s]
print(li)

#________________________________________________# list of list in string :

li = ["parikh", "rohan", "ankush"]
li_2d = [[p for p in ele] for ele in li]
print(li_2d)