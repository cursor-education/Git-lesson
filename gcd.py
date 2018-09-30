# Wrong gcd find 5 mistakes

def gcd(a:int, b:int): # maybe better, could be fifth mistake
    assert a >=0 and b >= 0 # first mistake
    while a and b:
        if a > b:
            a = a % b # second   mistake
        else:
            b = b % a # third   mistake
    return max (a, b) # fourth mistake

print(gcd(10, 0))
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))

# Examples

# gcd(10, 0) => 10
# gcd(123, 3) => 3
# gcd(1000000, 64) => 64
# gcd(0, 0) => 0
