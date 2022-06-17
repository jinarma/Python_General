def dupes(char_list):
	hashmap = {}
	for ele in char_list:
		if ele not in hashmap:
			hashmap[ele] = 1
		else:
			hashmap[ele] = hashmap[ele] + 1
	
	for j, k in hashmap.items():
		print(j, k)



list_char = ['k', 'a', 'y', 'o', 'r', 'z', 'q', 'z', 't', 'j', 'q', 'v', 'm', 'o', 'w', 'j', 't', 't', 'j', 'h', 'q', 'k', 'q', 't', 'v', 'k', 'z', 'f', 'e', 'p', 'b', 'n', 't', 'p', 't', 't', 'p', 'v', 's', 'g', 'k', 'x', 't', 'o', 'e', 'y', 'z', 'u', 'r', 'q', 'a', 'b', 'd', 'b', 'x', 'g', 'j', 'w', 'c', 'd', 'f', 'a', 'a', 's', 'm', 'y', 'l', 'e', 'i', 'k', 'x', 'j']

dupes(list_char)