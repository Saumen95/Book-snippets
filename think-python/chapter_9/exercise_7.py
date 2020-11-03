fin = open('words.txt')


def is_triplet(word):
    for index in range(len(word)-5):
        if word[index] == word[index+1]:
            if word[index+2] == word[index+3]:
                if word[index+4] == word[index+5]:
                    return True
    return False


count_match = 0
count_total = 0

for line in fin:
    word = line.strip()
    count_total += 1
    if is_triplet(word):
        count_match += 1
        print(word)

total = 'Total words: ' + str(count_total)
subtotal = 'Total matches: ' + str(count_match)
pct = str((100 * count_match) / count_total)[:5]
pct = pct + '% are triplets'

total = total.rjust(21)
subtotal = subtotal.rjust(21)
pct = pct.rjust(21)

print('=' * 21)
print(total)
print(subtotal)
print(pct)
print()


fin.seek(0)
