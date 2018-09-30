# Wrong gcd find 5 mistakes

def gcd(a, b):
    assert (a >= 0 and b >= 0 and (a != 0 or b != 0)), \
        "Check params, should be two or more integers, which are not all zero" #1
    while (a!=0 and b!=0): #2
        if a > b:
            a = a % b #3
        else:
            b = b % a #4
    return max(a, b) #5

# Examples

# print(gcd(10, 0)) #=> 10
# print(gcd(123, 3)) # => 3
# print(gcd(1000000, 64)) # => 64
# print(gcd(0, 0)) #=> exc
# print(gcd(54,24)) #=> 6