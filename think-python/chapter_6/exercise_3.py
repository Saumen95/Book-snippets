def first(word):
    # returns the first character of the argument
    return word[0]


def last(word):
    # returns the last character of the argument
    return word[-1]


def middle(word):
    # returns the middle characters of the argument (everything except first and last)
    return word[1:-1]


def is_palindrome(testword):
    if len(testword) <= 1:
        # recursion is done, so step out and be happy
        return True
    if first(testword) != last(testword):
        # if first and last don't match, it's not a palindrome
        return False
    return is_palindrome(middle(testword))
    # send back the middle bit for recursive testing


def is_palindrome2(testword):
    reverseword = ''
    for i in range(len(testword), 0, -1):
        # loop through the argument, right to left
        reverseword = reverseword + testword[i-1:i]
        # build a new string which is the reverse of the argument
    return testword == reverseword

test1 = 'madamimadam'
test2 = 'fruitful'
test3 = 'anna'

for i in (test1, test2, test3):
    print(' First function -', i, 'is a palindrome:', is_palindrome(i))
    print('Second function -', i, 'is a palindrome:', is_palindrome2(i))
    print()
