def is_power(a, b):
    """
    a is a power of b if:
      a is divisible by b
      a/b is a power of b
    """
    if a / b == b:
        return True
    if a % b > 0:
        return False
    return is_power(a / b, b)


first = 16
second = 4

print(first, 'is a power of', second, ':', is_power(first, second))
