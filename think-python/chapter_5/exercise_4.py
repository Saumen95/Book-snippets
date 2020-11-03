def recurse(n, s):
    """
    Sums the numbers between 1 and n, and adds them to s.
    For example, with (3, 2), it will iterate through 2 + (3 + 2 + 1), and return 8.
    """

    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 2)