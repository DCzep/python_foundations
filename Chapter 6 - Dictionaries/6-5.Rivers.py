major_rivers = {
    'nile': 'egypt',
    'mississippi': 'the united states',
    'danube': 'germany',
}

for key, country in major_rivers.items():
    print(f"The {key.title()} runs through {country.title()}.")

for river in major_rivers.keys():
    print(river.title())

for country in major_rivers.values():
    print(country.title())
