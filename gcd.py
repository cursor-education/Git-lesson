# Wrong gcd find 4 mistakes #5

def gcd(a, b):
    assert a >= 0 and b >= 0 #1
    while a and b:
        if a > b:
            a = a % b #2
        else:
            b = b % a #3
    return max(a, b) #4

# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0
