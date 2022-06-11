import turtle


t = turtle.Pen()

x0, y0, x1, y1 = map(int, input().split())
dx = abs(x0 - x1)
dy = abs(y0 - y1)

# find maximum difference
steps = max(dx, dy)

# calculate the increment in x and y
xinc = dx/steps
yinc = dy/steps

# start with 1st point
x = float(x0)
y = float(y0)


for i in range(steps):
	# append the x,y coordinates in respective list
	t.setpos(x, y)

	# increment the values
	x = x + xinc
	y = y + yinc
print(t.pos())
turtle.exitonclick()
