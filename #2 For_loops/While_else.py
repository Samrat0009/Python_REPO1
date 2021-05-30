#simple example:

i=1
while i<10:
    print(i)
    i=i+1
else:
    print("this will  be printeed at the end only once")

#complex example with Break as well:

i=1
while i<10:
    if i == 5:
        break
    print(i)
    i=i+1
else:
    print("i has reached 5 !!")           ## this time it will not be executed bcoz we used for!!


#if you still wanna print at end:

i=1
while i<10:
    if i == 5:
        break
    print(i)
    i=i+1

print("i has reached 5 !!")