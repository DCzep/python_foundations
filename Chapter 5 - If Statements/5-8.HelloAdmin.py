user_names = ['admin', 'dc3784', 'weaponx', 'cheezy', 'jrob']

for user in user_names:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
