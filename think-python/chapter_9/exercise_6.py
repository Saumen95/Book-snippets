"""
Write a function named uses_all that takes a word and a string of
required letters, and that returns True if the word uses all the
required letters at least once. How many words are there that use
all the vowels aeiou ? How about aeiouy ?
"""


fin = open('words.txt')


def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


count_match = 0
count_total = 0

for line in fin:
    word = line.strip()
    count_total += 1
    if is_abecedarian(word):
        count_match += 1
        print(word)

total = 'Total words: ' + str(count_total)
subtotal = 'Total matches: ' + str(count_match)
pct = str((100 * count_match) / count_total)[:5]
pct = pct + '% are alphabetical'

total = total.rjust(21)
subtotal = subtotal.rjust(21)
pct = pct.rjust(21)

print('=' * 21)
print(total)
print(subtotal)
print(pct)
print()

fin.seek(0)
