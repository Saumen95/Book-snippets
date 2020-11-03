import math


def mysqrt(a, x):
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root(upperlimit):
    a = 1.0
    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('--- ------------- ------------- ----')
    while a <= upperlimit:
        mysqrtxt = str(mysqrt(a, 3)) + ' ' * 13
        mathsqrtxt = str(math.sqrt(a)) + ' ' * 13
        sqrtdiff = abs(mysqrt(a, 3) - math.sqrt(a))
        print(a, mysqrtxt[0:13], mathsqrtxt[0:13], sqrtdiff)
        a += 1


test_square_root(9)
