def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter):
    counter = 0
    position = find(word, letter, 0)
    while position != -1 and position < len(word):
        position = find(word, letter, position + 1)
        counter += 1
    return counter


phrase = 'Every good boy deserves fun.'


print(count(phrase, 'e'))