a = 6	# 1001
b = 9	# 0110
c = [10]
print(bin(a))
print(bin(b))
print()
c.append(b & a)	# AND
c.append(b | a)	# OR
c.append(~b)	# NOT
c.append(~(b & a))	# NAND
c.append(~(b | a))	# NOR
c.append(b ^ a)	# XOR
for i in c:
	print(i, end=)
	print(bin(i))