def reverse_it(string):
    for i in range(len(string), 0, -1):
        print(string[i-1])


def reverse_it2(string):
    index = len(string) - 1
    while index >= 0:
        print(string[index])
        index -= 1


reverse_it('abc')

reverse_it2('123')
