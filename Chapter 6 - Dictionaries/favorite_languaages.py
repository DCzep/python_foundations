favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Looping through all key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# Looping through all the keys in a dictonary - this is default behavior don't need key()
for name in favorite_languages:
    print(name.title())
# Acces the value associated with any key, loop through a return a message
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
# key() method to find out if a particular person was polled
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a dictionary's keys in a particular order
# Use the sorted() function to get a copy of the keys in order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Loopoing through all values in a dictonary
# value() method to return a sequences of value without any keys.abs()

print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
