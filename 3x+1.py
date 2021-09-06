from matplotlib import pyplot as plt

x = []
y = []
def check(num):
	count = 0
	print("Starting number:", num, sep=' ')
	y.append(num)
	count+=1
	while num!=1:
		if num%2==0:
			num=num/2
			print(num)
			y.append(num)
			count+=1
		elif num%2!=0:
			num=3*num+1
			print(num)
			y.append(num)
			count+=1
	for n in range(count):
		x.append(n+1)
	plt.xticks(range(1, count+1))

check(141)
plt.plot(x, y, alpha=0.7)
for i_x, i_y in zip(x,y):	#used to plot values of graph on each point
	plt.text(i_x, i_y,'{:.0f}'.format(i_y))
plt.show()
