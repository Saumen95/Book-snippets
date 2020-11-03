prefixes = 'JKLMNOPQ'
suffix = 'ack'
name = ''

for letter in prefixes:
    name = letter
    if letter in 'OQ':
        name = name + 'u'
    name = name + 'ack'
    print(name)