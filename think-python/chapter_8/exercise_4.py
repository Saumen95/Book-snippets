"""
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, describe what the function actually does
(assuming that the parameter is a string).
"""

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
    # Returns True or False only for the first character, because
    # the 'return' statement exits the loop after the first test


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
    # Always returns 'True', as it's testing the literal string 'c'
    # Also, it's returning the literal string 'True', instead of
    # the value True



def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
    # Returns True or False only for the last character, because
    # the 'flag' variable is overwritten with each successive test.


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    # works properly; the flag variable will change to True when
    # it encounters the first lower case letter, and then remain
    # True (because FALSE OR TRUE = TRUE)


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True
    # This will return False (and exit the loop) when it encounters
    # the first non-lowercase character. It will return True only
    # if *every* character is lower (because that's the only way
    # it will reach the end of the loop).


print(any_lowercase1('Banana'))
print(any_lowercase2('Banana'))
print(any_lowercase3('Banana'))
print(any_lowercase4('Banana'))
print(any_lowercase5('Banana'))