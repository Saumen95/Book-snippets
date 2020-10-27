car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_decending = sorted(car_ages,reverse=True)
oldest, second_oldest, *others = car_ages_decending
print(oldest,second_oldest, others)
