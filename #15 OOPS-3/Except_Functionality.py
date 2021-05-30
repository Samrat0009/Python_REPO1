# Error inheriting from Parent Class : Ex : below parent class = ZeroDivisionError

class ZeroDenominatorError(ZeroDivisionError):   #This is how you inherit from parent error!
    pass


while True:
    try:
        n = input('Enter the numerator :')
        num = int(n)
        n = input('Enter the denominator :')
        denom = int(n)
        if denom == 0:                              # this is how you raise your own exception !!!
            raise ZeroDenominatorError()
        value = num / denom
        print(value)

    except ValueError:
        print("Numerator and Denominator should be integers")
    except ZeroDenominatorError:                        # NOTE : since ZeroDivision is superclass of ZeroDenominator error
        print("ZeroDenominatorError is raised")         #        So, if you type it after ZeroDivision Error or if you don't write it at all,
    except ZeroDivisionError:                           #        it will have no significance BUT if you write in this order it will show
        print("Division by zero is not allowed")        #        ZeroDenominatorError !!
    except:
        print("some exception is raised")
