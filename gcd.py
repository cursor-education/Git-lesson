# Wrong gcd find 5 mistakes

def gcd(a, b): # mistake 1 - we do not specify explicitly that the type must be int
    assert a <= 0 and b >= 0  # mistake 2 - a will be asserted to be *less* than 0 in this case;
    # mistake 3 - there is no error message in case assertion fails - it is optional, but still better to have it
    while a and b: # mistake 4 - eternal loop if initially a or b is not 0
        if a > b: # mistake 5 - risk of dividing by zero if b = 0
            a = a / b
        else: # same mistake 5 if a =0
            b = b / a
    return min(a, b)

# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0