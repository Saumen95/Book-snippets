"""
In 1939 Ernest Vincent Wright published a 50,000 word novel called
Gadsby that does not contain the letter “e”. Since “e” is the most
common letter in English, that’s not easy to do.

Write a function called has_no_e that returns True if the given word
doesn’t have the letter “e” in it.

Modify your program from the previous section to print only the
words that have no “e” and compute the percentage of the words in
the list that have no “e”.
"""


fin = open('words.txt')


def has_no_e(word):
    return word.find('e') == -1


count_total = 0
count_match = 0


for line in fin:
    word = line.strip()
    count_total += 1
    if has_no_e(word):
        count_match += 1
        print(word)


total = 'Total words: ' + str(count_total)
subtotal = 'Total matches: ' + str(count_match)
pct = str(100 * count_match // count_total) + '% have no "e"'

total = total.rjust(21)
subtotal = subtotal.rjust(21)
pct = pct.rjust(21)

print('=' * 21)
print(total)
print(subtotal)
print(pct)