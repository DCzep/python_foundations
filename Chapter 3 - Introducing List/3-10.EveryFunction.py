fav_vacations = ['ireland', 'france', 'slovenia',
                 'hawaii', 'hilton head', 'poland']

# Accessing Elements in List
print(fav_vacations[0])
print(fav_vacations[4].title())
print(fav_vacations[-1].title())

# Using Individual Values from a List
message = f'My favorite trip with Tara was to {fav_vacations[0].title()}.'
print(message)

# Modifying, Adding, and Removing Elements
fav_vacations[5] = 'denmark'
print(fav_vacations)

# Adding Elements to a List
fav_vacations.append('poland')
print(fav_vacations)

# Inserting Elements into a List
fav_vacations.insert(0, 'germany')
print(fav_vacations)

# Removing an Element from list
del fav_vacations[2]
print(fav_vacations)

# Removing an Item using the pop() method
popped_fav = fav_vacations.pop()
print(fav_vacations)
print(popped_fav)
print(f'Our trip to {popped_fav.title()} was really interesting.')

# Popping Items from Any Position in a List
first_trip = fav_vacations.pop(2)
print(f'The first trip to Europe was going to {first_trip.title()}.')

# Removing an item by Value
print(fav_vacations)
pre_adult = 'hawaii'
fav_vacations.remove(pre_adult)
print(fav_vacations)
print(f'\nMy trip to {pre_adult.title()} occured when I was in 8th grade')
# Sorting a List Permanently with the sort() Method
print(fav_vacations)
fav_vacations.sort()
print(fav_vacations)
# Sort List Temporarily with the sorted() function
fav_vacations = ['ireland', 'france', 'slovenia',
                 'hawaii', 'hilton head', 'poland']
print(fav_vacations)
print("\nHere is the sorted list:")
print(sorted(fav_vacations))
print(fav_vacations)

# Print in reverse order
fav_vacations.reverse()
print(fav_vacations)

# Finding the Length
length = len(fav_vacations)
print(f'I have enjoy {length} vacations.')

