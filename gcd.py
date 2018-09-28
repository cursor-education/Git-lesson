def gcd(a, b):
    assert a >= 0 and b >= 0        # 1st bug a<=0
    while a and b:
        if a > b:
            a = a % b               # 2nd bug a%b  
        else:
            b = b % a               # 3rd bug b%a
    return max(a, b)                # 4th bug not min() but max()

                                # Expected results :
if __name__=='__main__':            # maybe 5th bug
    print(gcd(10, 0))           # => 10
    print(gcd(123, 3))          # => 3
    print(gcd(1000000, 64))     # => 64
    print(gcd(0, 0))            # => 0