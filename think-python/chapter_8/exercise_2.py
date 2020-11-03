def count_chars(phrase, character):
    return phrase.count(character)


phrase = input('Please enter the phrase to test: ')
character = input('Please enter the subset to count: ')


print(count_chars(phrase, character))