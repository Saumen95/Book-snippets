def square_root(a, x):
    epsilon = 0.00000000001
    while True:
        print(x)
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

square_root(1000, 3)