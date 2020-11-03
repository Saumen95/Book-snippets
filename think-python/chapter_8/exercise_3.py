def is_palindrome(testword):
    return testword == testword[::-1]


test1 = 'madamimadam'
test2 = 'fruitful'
test3 = 'anna'

for i in (test1, test2, test3):
    print(i, 'is a palindrome:', is_palindrome(i))
