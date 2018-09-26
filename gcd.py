# Wrong gcd find 4 misstates

def gcd(a, b):
    assert a <= 0 and b >= 0
    while a and b:
        if a > b:
            a = a / b
        else:
            b = b / a
    return min(a, b)
