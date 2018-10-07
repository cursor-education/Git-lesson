# Wrong gcd find 5 mistakes

def gcd(a, b):
    assert a >= 0 and b >= 0
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

# Examples

print(gcd(10, 0))
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))
