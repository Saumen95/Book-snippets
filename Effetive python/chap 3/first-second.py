first, second = 1, 2
assert first == 1
assert second == 2

def my_func():
    return 1, 2


first, second = my_func()
assert first == 1
assert second == 2
