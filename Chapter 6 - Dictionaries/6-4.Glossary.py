program_words = {
    'variables': 'labels that you can assign to values',
    'strings': 'a series of characters',
    'whitespace': 'any nonprinting characters',
    'floats': 'any number with a decimal',
    'constant': 'a variables whose value stays the same throughout the life of a program',
    'dictionary': 'a collection of key-value pairs',
    'boolean': 'value that is either true or false',
    'tuple': 'values that cannot change, and immutable list',
    'slice': 'specific group of items in a list',
    'list': 'a collection of items in a pacticular order'
}

for key, meaning in program_words.items():
    print(f"\n{key.title()}:")
    print(f"\t{meaning.title()}")
