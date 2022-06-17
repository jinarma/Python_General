from matplotlib import pyplot as plt

# DDA Function for line generation


def DDA(x0, y0, x1, y1):

	# find absolute differences
	dx = abs(x0 - x1)
	dy = abs(y0 - y1)

	# find maximum difference
	steps = max(dx, dy)

	slope = abs(dy/dx)

	# start with 1st point
	x = float(x0)
	y = float(y0)

	# make a list for coordinates
	x_coorinates = []
	y_coorinates = []

	for i in range(steps-1):
		# append the x,y coordinates in respective list
		x_coorinates.append(abs(x))
		y_coorinates.append(abs(y))

		if slope < 1:
		# increment the values
			x += 1
			y = y + slope
		
		if slope > 1:
			y += 1
			x = x + slope

		if slope == 1:
			x += 1
			y += 1

	# plot the line with coordinates list
	plt.plot(y_coorinates, x_coorinates, marker="o", markersize=1, markerfacecolor="green")
	plt.show()


if __name__ == "__main__":

	# coordinates of 1st point
	x0, y0 = 0, 0

	# coordinates of 2nd point
	x1, y1 = 4, 6
	DDA(x0, y0, x1, y1)
