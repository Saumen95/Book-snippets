def get_stats(number):
    minimum = min(number)
    maximum = max(number)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')
