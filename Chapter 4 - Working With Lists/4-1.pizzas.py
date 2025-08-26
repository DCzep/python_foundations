# Daniel Czepiga
# Pizza List
fav_pizzas = ['plain', 'sausage', 'pepperoni', 'garlic']
for pizza in fav_pizzas:
    # Loop to list just the name of the pizza in the list
    print(pizza.title())
    # Print a statement for each pizza in the list that I like
    print(f'I like {pizza} pizza.')
message = f'My favorite type of pizza is {fav_pizzas[2]}, however I do enjoy a pie with both {fav_pizzas[1]} and {fav_pizzas[3]}. I will eat {fav_pizzas[0]} anytime.'
print(message)
print('I really love pizza! I could it every night for dinner.')
