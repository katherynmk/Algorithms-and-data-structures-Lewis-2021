#R-4.3 Draw the recursion trace for the computation of power(2,18), using the repeated squaring algorithm, as implemented in Code Fragment 4.12.

def power(a,b):

    if b == 0:
        return 1

    else:

        instant = power(a, b//2)

        finalpower = instant ** instant

        if b%2 == 1:
            finalpower = a * finalpower 

        return finalpower

print (power(2,0))