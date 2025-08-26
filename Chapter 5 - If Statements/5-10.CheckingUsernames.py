current_users = ['Mav35dc', 'Jrob', 'Weaponx', 'Dc3784', 'Cheesy']
new_users = ['LtDan', 'Achavelli', 'Tripple', 'dc3784', 'Jrob']

current_users = [element.lower() for element in current_users]
new_users = [element.lower() for element in new_users]
for user in new_users:
    if user in current_users:
        print("This username is taken, please eneter a new one.")
    else:
        print("That username is available.")
