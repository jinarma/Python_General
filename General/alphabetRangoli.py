""" 

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""

def print_rangoli(size):
	# your code goes here
	# ASCII 97 (a) - 122 (z)
	ascii_a = 97
	for i in range(size-1, -1, -1):
		if i >= 0:
			print(chr(ascii_a+i).center())
		if i == 0:
			for j in range(1, size):
				print(chr(ascii_a+j))


if __name__ == '__main__':
	n = int(input())
	print_rangoli(n)
