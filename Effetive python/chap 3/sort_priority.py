def sort_priority(number, group):
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)

    number.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)
