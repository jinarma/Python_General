

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
new_dict = {}
for t_guest_name, t_guest_plus in Taylors_guests.items():
	for r_guest_name, r_guest_plus in Rorys_guests.items():
		if r_guest_name != t_guest_name:
			Rorys_guests[t_guest_name] = t_guest_plus
		else:
			continue
print(Rorys_guests.keys())
print(Taylors_guests.keys())