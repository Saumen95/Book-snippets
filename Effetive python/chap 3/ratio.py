def avg(numbers):
    avarage = sum(numbers) / len(numbers)
    scaled = [x / avarage for x  in numbers]
    scaled.sort(reverse=True)
    return scaled


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
longest, *middle, shortest = avg(lengths) # catch  all starred expression

print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')
