# Raising our own exceptions :

# Ex : say if the denominator has been give 0 and you want there to be an error printed !


class ZeroDenominatorError(Exception):   #This is how you integrate a new type of error in Python !
    pass


while True:
    try:
        n = input('Enter the numerator :')
        num = int(n)
        n = input('Enter the denominator :')
        denom = int(n)
        if denom == 0:                              # this is how you raise your own exception !!!
            #raise ZeroDivisionError('write a custom message')   OR
            raise ZeroDenominatorError('Denominator should not be zero')
        value = num / denom
        print(value)
    except ValueError:
        print("Numerator and Denominator should be integers")
    except ZeroDenominatorError:
        print("ZeroDenominatorError is raised")
    except ZeroDivisionError:
        print("Division by zero is not allowed")




