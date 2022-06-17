x, r, y = 0, 50, 50

d = 3 - 2 * r

while x < y:
	if d < 0:
		x += 1
		d += 4*x+6
	else:
		d += 4*(x+y)+10
		x += 1
		y -= 1
		
	print(x, y)
