def caseless_sort(tup: tuple) -> tuple:
	return (tup[0].lower(), -tup[1])		# returns (x, y) i.e if x are same, then comparison goes to y
	# adding the negative at y, we instruct it to sort in reverse i.e. descending by deault


tuple_list = [('a', 2), ('B', 6), ('A', 1), ('c', 5)]
print(tuple_list)
print(sorted(tuple_list, key=caseless_sort))