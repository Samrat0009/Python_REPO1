a = 'parikh' == 'parikh'

print(a)

# now since alphabets are represented by there ascii values, so if :

a = 'rarikh' >= 'parikh'            # because ascii value of r is > ascii(p) !
print(a)

a = 'Rarikh' >= 'parikh'            # because ascii(capital letters) is < ascii(small letters) !!!
print(a)