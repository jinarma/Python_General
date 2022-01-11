from random import randint as rd

def binarySearch(ls, num):
	if num > ls[-1]:
		print('Not in this list')
	count = len(ls)
	a = 0
	b = count
	c = (a+b)//2
	prevC = -1
	while c != prevC:
		if num == ls[c]:
			print(num, 'at index', c)
			return
		elif num < ls[c]:
			b = c
		elif num > ls[c]:
			a = c
		prevC = c
		c = (a+b)//2
	print('Number doesn\'t exist in the list.')
	return

# Driver
if __name__ == '__main__':
	ls = list((0+rd(1, 2000)) for i in range(100))
	ls.sort()
	search_num = int(input('Number to search: '))
	binarySearch(ls, search_num)
