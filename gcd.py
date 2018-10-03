# Wrong gcd find 5 mistakes
def gcd(a, b):
    assert a >= 0 and b >= 0    #1st bug: a <= 0
    while a and b:
        if a > b:
            a = a % b           #2nd bug: a / b
        else:
            b = b % a           #3rd bug: b / a
    return max(a, b)            #4th bug: min()

print(gcd(10, 0))               #5th bug: The programm doesn't have print() function
print(gcd(123, 3))
print(gcd(1000000, 64))
print(gcd(0, 0))

