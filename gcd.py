# Wrong gcd find 5 mistakes <- maybe this is fifth mistakes?

def gcd(a, b):
    assert a >= 0 and b >= 0
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


print(gcd(10, 0))
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))


# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0
