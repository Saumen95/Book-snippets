"""
Write a function named uses_all that takes a word and a string of
required letters, and that returns True if the word uses all the
required letters at least once. How many words are there that use
all the vowels aeiou ? How about aeiouy ?
"""


fin = open('words.txt')


def uses_only(test, available):
    for letter in available:
        if letter not in test:
            return False
    return True


require = input('Enter the required characters, or 1234 to stop: ')

while require != '1234':

    count_match = 0
    count_total = 0

    for line in fin:
        word = line.strip()
        count_total += 1
        if uses_only(word, require):
            count_match += 1
            print(word)

    total = 'Total words: ' + str(count_total)
    subtotal = 'Total matches: ' + str(count_match)
    pct = str((100 * count_match) / count_total)[:5]
    pct = pct + '% include ' + require

    total = total.rjust(21)
    subtotal = subtotal.rjust(21)
    pct = pct.rjust(21)

    print('=' * 21)
    print(total)
    print(subtotal)
    print(pct)
    print()

    fin.seek(0)

    require = input('Enter the characters to require, or 1234 to stop: ')


