# Exception Handling !


# method : Try and Except : try the code and look for any exception !
#try:
#    n = input("Enter the numerator :")
#    num = int(n)
#
#   n = input("Enter the denominator :")         # suppose we enter a str & not an int
#    den = int(n)
#
#    print(num / den)

# so to eliminate the value error:

#except ValueError:             # if you don't specify which error then every error will give the below statement!
#    print("both num and den should be integers")

# Now to get input form user again and again till correct :


while True:
    try:
        n = input("Enter the numerator :")
        num = int(n)

        n = input("Enter the denominator :")  # suppose we enter a str & not an int
        den = int(n)

        print(num / den)

    # so to eliminate the value error:

    except ValueError:  # if you don't specify which error then every error will give the below statement!
        print("both num and den should be integers")
