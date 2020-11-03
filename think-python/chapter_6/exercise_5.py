def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

test1 = 4029
test2 = 11139
print('The greatest common denominator of', test1, '&', test2, 'is :', gcd(test1, test2))