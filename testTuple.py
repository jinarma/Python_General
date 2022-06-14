def caseless_sort(tup: tuple) -> tuple:
	return (tup[0].lower(), tup[1])		# returns (x, y) i.e if x are same, then comparison goes to y


tuple_list = [('a', 2), ('B', 6), ('A', 1), ('c', 5)]
print(tuple_list)
print(sorted(tuple_list, key=caseless_sort))