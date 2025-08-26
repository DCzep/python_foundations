guest_list = ['barbara czepiga', 'john czepiga', 'faith czepiga']
print(f"Hello {guest_list[0].title()}, please join your son for dinner.")
print(f"Hello {guest_list[1].title()}, join me for dinner soon.")
print(f"Hello {guest_list[2].title()}, join your dad for dinner.")

print("Good news, we found a bigger table and I will be inviting more guests.")

guest_list.insert(0, 'walter czepiga')
guest_list.insert(2, 'carolynn czepiga')
guest_list.append('tara czepiga')

print(f"Hello {guest_list[0].title()}, you are invited to the Czepiga dinner.")
print(f"Hello {guest_list[1].title()}, you are invited to the Czepiga dinner.")
print(f"Hello {guest_list[2].title()}, you are invited to the Czepiga dinner.")
print(f"Hello {guest_list[3].title()}, you are invited to the Czepiga dinner.")
print(f"Hello {guest_list[4].title()}, you are invited to the Czepiga dinner.")
print(f"Hello {guest_list[5].title()}, you are invited to the Czepiga dinner.")

print("Apologies everyone, the talbe will not arrive in time and therefore can only bring two people to dinner.")

first_guest = guest_list.pop(5)
print(f"I apologize {first_guest.title()} but I cannot have you for dinner.")
second_guest = guest_list.pop(4)
print(f"I apologize {second_guest.title()} but I cannot have you for dinner.")
third_guest = guest_list.pop(3)
print(f"I apologize {third_guest.title()} but I cannot have you for dinner.")
fourth_guest = guest_list.pop(2)
print(f"I apologize {fourth_guest.title()} but I cannot have you for dinner.")

print(f"{guest_list[0].title()}, join us still for dinner.")
print(f"{guest_list[1].title()}, join us still for dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)
