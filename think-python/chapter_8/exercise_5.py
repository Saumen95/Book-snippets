def rotate_letter(letter, steps):

    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    delta = ord(letter) - start
    new_letter_ord = start + (delta + steps) % 26
    return chr(new_letter_ord)


def rotate_word(word, steps):
    new_word = ''
    for letter in word:
        new_word = new_word + rotate_letter(letter, steps)
    return new_word


print(rotate_word('Banana', 1))
print(rotate_word('CHEER', 7))
print(rotate_word('Melon', -10))
