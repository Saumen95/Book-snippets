import math

def hypotenuse(a, b):
    # sovles for the length of the hypotenuse of a right triangle
    # given the lengths of the other two sides (a and b).
    a_sqrd = a**2
    b_sqrd = b**2
    hyp = math.sqrt(a_sqrd + b_sqrd)
    return hyp

a = 6
b = 8
print('opposite', a, 'adjacent', b, 'hypotenuse', hypotenuse(a, b))