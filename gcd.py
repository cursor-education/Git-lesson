# Wrong gcd find 5 mistakes

def gcd(a, b):
    assert a > 0 or b >= 0
    if b == 0:
       return a

    else:
        return gcd(b, a % b)


print(gcd(10, 0))
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))
