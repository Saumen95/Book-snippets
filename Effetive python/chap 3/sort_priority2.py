def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            return (0, x)

        else:
            return (1, x)
    numbers.sort(helper)
    return found


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = group = {2, 3, 5, 7}
found = sort_priority2(numbers, group)
