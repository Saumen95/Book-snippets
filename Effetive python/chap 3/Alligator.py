def get_stats(number):
    minimum = min(number)
    maximum = max(number)
    count = len(number)
    avg = sum(number) / len(number)

    sorted_num = sorted(number)
    mid = count // 2
    if count // 2 == 0:
        lower = sorted_num[mid - 1]
        upper = sorted_num[mid + 1]
        median = (lower + upper) / 2

    else:
        median = mid

    return minimum, maximum, avg, median, count

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum, avg, median, count = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {avg}, Median: {median}, Count {count}')
