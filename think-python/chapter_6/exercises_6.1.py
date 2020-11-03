def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 'input error'

for i in range(3):
    for j in range(3):
        print(i, j, compare(i, j))
