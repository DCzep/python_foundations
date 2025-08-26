# Daniel Czepiga
# Animals
# List of animals that are simliar because they are predator cats
sim_animals = ['lion', 'tiger', 'puma', 'cougar', 'bobcat']
for animal in sim_animals:
    print(animal.title())
    print(f'The {animal} is a big cat and a preator.\n')
print('All of these animals come from a common ancestor.')

print("The first three items in the list are:")
for animal in sim_animals[0:3]:
    print(animal.title())

print("Three items from the middel of the list are:")
for animal in sim_animals[1:4]:
    print(animal.title())

print("The last three items in the list are:")
for animal in sim_animals[2:5]:
    print(animal.title())
