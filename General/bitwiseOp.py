a = 5	# 0101
b = 9	# 1001
c = []
print(a, bin(a))
print(b, bin(b))
print(a+b, bin(a+b))
print()
# c.append(b & a)	# AND
# c.append(b | a)	# OR
c.append(~b)	# NOT
# c.append(~(b & a))	# NAND
# c.append(~(b | a))	# NOR
# c.append(b ^ a)	# XOR
# c.append(~(a ^ b)) # XNOR
# c.append((~(a ^ b))+1) # 2s compliment
for i in c:
	print(i, bin(i), sep=' ')
print(c)