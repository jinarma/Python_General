

poem = "But soft what light through yonder window breaks\nIt is the east and Juliet is the sun\nArise fair sun and kill the envious moon\nWho is already sick and pale with grief"
count = {
	'but': 1,
	'soft': 1,
	'what': 1,
	'light': 1,
	'through': 1,
	'yonder': 1,
	'window': 1,
	'breaks': 1,
	'it': 1,
	'is': 3,
	'the': 3,
	'east': 1,
	'and': 3,
	'juliet': 1,
	'sun': 2,
	'arise': 1,
	'fair': 1,
	'kill': 1,
	'envious': 1,
	'moon': 1,
	'who': 1,
	'already': 1,
	'sick': 1,
	'pale': 1,
	'with': 1,
	'grief': 1
}

# creates a List of Key elements in ascending alphabetical order
just_sorted_count = sorted(count)
print(f'just_sorted_count - {just_sorted_count}')

# creates a Dict of count in ascending order of Keys
sorted_with_dict_count = dict(sorted(count.items()))
print(f'sorted_with_dict_count - {sorted_with_dict_count}')

# creates a Dict of count in ascending order of Values
sorted_with_dict_and_values_count = dict(sorted(count.items(), key= lambda x: x[1]))
print(f'sorted_with_dict_and_values_count - {sorted_with_dict_and_values_count}')

def sort_based_on_values(key_value_pair: set) -> int:
	return key_value_pair[1]

sorted_with_dict_and_values_count_using_normal_function = dict(sorted(count.items(), key=sort_based_on_values))
print(f'sorted_with_dict_and_values_count_using_normal_function - {sorted_with_dict_and_values_count_using_normal_function}')

# creates a Dict of count in ascending order of Values but also if Values are equal then based on alphabetical order of Keys
# can't think of anything rn
