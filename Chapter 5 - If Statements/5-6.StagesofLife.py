age = 39
if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

age = 1
if age < 2:
    stage = 'baby'
elif age >= 2 and age < 4:
    stage = 'toddler'
elif age >= 4 and age < 13:
    stage = 'kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f"The person is a {stage}.")
