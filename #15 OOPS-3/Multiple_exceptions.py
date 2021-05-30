while True:
    try:
        n = input("Enter the numerator :")
        num = int(n)

        n = input("Enter the denominator :")  # suppose we enter a str & not an int
        den = int(n)

        print(num / den)

    # so to eliminate the value error:

    except (ValueError,ZeroDivisionError):  # this means if you get either of the errors it would print the following!
        print("both num and den should be integers")
