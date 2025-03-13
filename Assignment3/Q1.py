
a = int(input("Enter a number: "))

def fact(f):
    retVal = f
    if(f == 1):
        return f
    else:        
        retVal =  retVal * fact(f-1)
    return retVal

print("Factorial of {} is: {}".format(a,fact(a)))
    