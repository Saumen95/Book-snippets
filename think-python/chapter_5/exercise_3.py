def is_triangle(a, b, c):
    """
    The sum of all three sides, minus the length of the longest side,
    yields the sum of the lengths of the two shortest sides.
    """
    if (a + b + c) - max(a, b, c) < max(a, b, c):
        print('No')
    else:
        print('Yes')

def gather_inputs():
    print('Please enter the lenths of three sides of a triangle.')
    a = int(input('Side 1: '))
    b = int(input('Side 2: '))
    c = int(input('Side 3: '))
    print()
    print('Testing... can these three sides define a triangle?', end=' ')
    is_triangle(a, b, c)

gather_inputs()