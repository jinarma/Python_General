x1, y1 = 7, 8
x2, y2 = 1, 18

dx = abs(x2-x1)
dy = abs(y2-y1)

error = 2 * dy - dx

x = x1
y = y1

print(f'({x}, {y})')
while x <= x2 or y <= y2:

	if error >= 0:
		x += 1
		y += 1
		error = error - 2 * dx + 2 * dy

	elif error < 0:
		x += 1
		error = error + 2 * dy
		
	print(f'({x}, {y})')