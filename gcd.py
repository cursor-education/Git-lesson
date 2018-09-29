# Wrong gcd find 5 mistakes

def gcd(a: int, b: int):       #1
    assert a > 0 and b > 0     #2
    while a and b:
        if a > b:
            a = a % b          #3
        else:
            b = b % a          #4
    return max(a, b)           #5

# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0
