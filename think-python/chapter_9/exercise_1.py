"""
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
"""

fin = open('words.txt')

count = 0

for line in fin:
    word = line.strip()
    if len(word) > 20:
        count += 1
        print(word)

if count > 0:
    total = 'Total matches: ' + str(count)
    total = total.rjust(21)
    print('=' * 21)
    print(total)
