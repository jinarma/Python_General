import turtle
colors = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.hideturtle()
for x in range(101):
	t.pencolor(colors[x % 6])
	t.width(x//100 + 1)
	if x%20 == 0:
		turtle.title(f'There are {x} lines on the screen RN')
	t.forward(x)
	t.left(59)
turtle.done()
turtle.exitonclick()
