
def gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    while a and b:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

print(gcd(10, 0))
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))
