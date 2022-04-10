def totalSearchTime(books_list, books_to_find):
	total_time = 0
	for i, book in enumerate(books_to_find):
		for j, check in enumerate(books_list):
			if book == check:
				total_time += j
				break
			else:
				continue
	return total_time

print(totalSearchTime([4, 5, 6, 7, 1, 2, 3], [7, 4, 6]))