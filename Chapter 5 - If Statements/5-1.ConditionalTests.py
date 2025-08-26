movie = 'superbad'
print("Is movie equal == 'superbad'? I predict True.")
print(movie == 'superbad')

print("\nIs movie == 'batman'? I predict False.")
print(movie == 'batman')

print("\nIs movie equal == 'Superbad'? I predict False.")
print(movie == 'Superbad')

print("\nIs movie equal == 'Superbad? I predict True using the title method.")
print(movie.title() == 'Superbad')

requested_movie = 'superman'

if requested_movie != 'superbad':
    print("\nThis is not the movie you want to watch. You requested Superman so it's false.")

age = 18
print("\nIs your age equal == 21? I predict False.")
print(age == 21)

print("\nIs your age less than or equal 18? I predict True.")
print(age <= 18)

print("\nIs your age greater than 21 or greater than 15. I predict True.")
print(age > 21 or age > 15)

requested_brand = ['nike', 'addidas', 'puma', 'old navy']
brand = 'nike'
if brand not in requested_brand:
    print(f"\n{brand.title()}, this brand is not on the approved vendor list.")
else:
    print(f"\n{brand.title()}, this brand is on the approved vendor list.")
print("This is true, the brand is in the list.")
