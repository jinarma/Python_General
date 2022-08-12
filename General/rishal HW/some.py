import csv
import os
import matplotlib.pyplot as plt

new_path = os.path.join(os.path.dirname(__file__), 'all-hands.csv')
num_list_2d = []
def CSV_Creation():
	with open(new_path, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			row = list(map(int, row))
			num_list_2d.append(row)
	return num_list_2d
# print(os.path.dirname(__file__))
# print(new_path)
CSV_Creation()
# print(num_list_2d)
x = []
y = []
temp_x = []
temp_y = []
# print(num_list_2d[0])
# print(num_list_2d[1])
for ele in num_list_2d:
	for i in range(0,ele[-1],2):
		if i < len(ele):
			x.append(ele[i])
			y.append(ele[i+1])
# 	print(x)
# 	print()
# 	print()
# 	print()
	temp_x.append(x)	
	temp_y.append(y)	
for ele in temp_x:
	print(ele)
	print()
# plt.plot(temp_x[0], temp_y[0])
# # plt.show()
