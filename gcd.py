# Wrong gcd find 5 mistakes

def gcd(a, b): # mistake 1 - we do not specify explicitly that the type must be int
    assert a <= 0 and b >= 0  # mistake 2 - a will be asserted to be *less* than 0 in this case;
    # mistake 3 - there is no error message in case assertion fails - it is optional, but still better to have it
    while a and b:
        if a > b:
            a = a / b  # mistake 4 - we have to use modulo in order to know both the remainder and to escape the loop once the remainder would be 0
        else:
            b = b / a  # same mistake 4
    return min(a, b)  # mistake 5 - should be max, as we are looking for the *greatest* divisor

# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0