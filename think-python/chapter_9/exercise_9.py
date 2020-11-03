def are_reversed(s, t):
    """
    Checks to see if the parameter is a palindrome.
    :param s: string
    :return: bool
    """
    return str(s).zfill(2) == str(t).zfill(2)[::-1]


def num_matches(diff, flag=False):
    """
    Counts the number of times that the mother and daughter have
    reversed ages, given a difference between them of (diff) years.
    
    Assumes that each year the difference will be +/- 1 (e.g., if
    the daughter is 30 and the mother is 50, and the mother's
    birthday is first, they'll be 21 years apart - then 20 years
    again when the daughter has her birthday).
    
    Also assumes the mother won't live past 120.
    
    :param diff: difference, in years. 
    :return: int - the count of times their ages reverse.
    """
    daughter = 0
    count = 0

    while True:
        mother = daughter + diff

        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count += 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter += 1
    return count


def check_diffs():
    """
    loop through possible age differences, printing the difference
    in age, and a table of ages, if there are 8 or more possible
    matches.
    :return: 
    """
    diff = 10
    while diff < 70:
        n = num_matches(diff)
        if n >= 8:
            print(diff, n)
        diff += 1

check_diffs()
print('daughter','mother')
num_matches(18, True)