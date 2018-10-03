# Wrong gcd find 5 mistakes

def gcd(a:int, b:int):
    assert a >= 0 and b >= 0, "Please do not use negative integers"
    remainder = 1
    while remainder:
        if a == 0 or b == 0:
            return max(a,b)
        elif a > b:
            remainder = a % b
            a = a / b
        else:
            b = b / a
            remainder = b % a
    return min(a, b)

# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0

print(gcd(10, 0))
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))