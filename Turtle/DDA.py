import turtle


x0, y0, x1, y1 = map(int, input().split())
dx, dy = x1-x0, y1-y0

t = turtle.Pen()
steps = 0
if abs(dy) > abs(dx):
	steps = abs(dy)
else:
	steps = abs(dx)

x, y = x0, y0
m=dy/dx
for i in range(steps):
	if x != x1 and y != y1:
		if m < 1:
			x = round(1+x)
			y = round(m+y)
			t.setpos(x, y)
		elif m == 1:
			x = round(1+x)
			y = round(1+y)
			t.setpos(x, y)
		elif m > 1:
			x = round(1/m+x)
			y = round(1+y)
			t.setpos(x, y)
	else:
		break
print(t.pos())
turtle.exitonclick()