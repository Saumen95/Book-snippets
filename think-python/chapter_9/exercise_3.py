"""
Write a function named avoids that takes a word and a string of
forbidden letters, and that returns True if the word doesn’t use
any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden
letters and then print the number of words that don’t contain any of
them. Can you find a combination of 5 forbidden letters that excludes
the smallest number of words?
"""


fin = open('words.txt')


def avoids(test, forbidden):
    for letter in forbidden:
        if letter in test:
            return False
    return True


avoid = input('Enter the characters to avoid, or 1234 to stop: ')

while avoid != '1234':

    count_match = 0
    count_total = 0

    for line in fin:
        word = line.strip()
        count_total += 1
        if avoids(word, avoid):
            count_match += 1
            print(word)

    total = 'Total words: ' + str(count_total)
    subtotal = 'Total matches: ' + str(count_match)
    pct = str((100 * count_match) / count_total)[:5]
    pct = pct + '% avoid ' + avoid

    total = total.rjust(21)
    subtotal = subtotal.rjust(21)
    pct = pct.rjust(21)

    print('=' * 21)
    print(total)
    print(subtotal)
    print(pct)
    print()

    fin.seek(0)

    avoid = input('Enter the characters to avoid, or 1234 to stop: ')


