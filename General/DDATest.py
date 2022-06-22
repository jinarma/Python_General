from matplotlib import pyplot as plt

# DDA Function for line generation


def DDA(x0, y0, x1, y1):

	# find absolute differences
	dx = x1 - x0
	dy = y1 - y0

	# find maximum difference
	steps = max(abs(dx), abs(dy))

	slope = dy/dx

	# start with 1st point
	x = float(x0)
	y = float(y0)

	# make a list for coordinates
	x_coorinates = []
	y_coorinates = []

	x_inc = 1 if dx >= 0 else -1
	y_inc = 1 if dy >= 0 else -1

	for _ in range(steps+1):
		# append the x,y coordinates in respective list
		x_coorinates.append(round(x))
		y_coorinates.append(round(y))

		# case when slope is negative and moving towards zero
		if slope >= -1 and slope <= 0:
			x += x_inc
			y = y + slope * x_inc

		# case when slope is negative and moving towards negative infinity
		elif slope < -1:
			y += y_inc
			x = x + y_inc/slope

		# case when slope is positive and moving towards zero
		elif slope <= 1:
			x += x_inc
			y = y + slope * x_inc
		
		# case when slope is positive and moving towards positive infinity
		elif slope > 1:
			y += y_inc
			x = x + y_inc/slope

		# if slope == 1:
		# 	x += 1
		# 	y += 1

	# plot the line with coordinates list
	plt.plot(x_coorinates, y_coorinates)
	plt.show()
	print(x_coorinates, y_coorinates)


if __name__ == "__main__":

	# coordinates of 1st point
	x0, y0 = 8, 13

	# coordinates of 2nd point
	x1, y1 = 4, 6
	DDA(x0, y0, x1, y1)
