num_of_colleges, num_of_students = list(map(int, input().split()))
temp_seats = list(map(int, input().split()))
num_of_seats = {}
student_details = []

for i in range(num_of_colleges):
	num_of_seats[f'C-{i+1}'] = temp_seats[i]

for j in range(num_of_students):
	temp = []
	stu_deets = input().split(',')
	temp.append(int((stu_deets[0].split('-'))[1]))	# ID
	temp.append(float(stu_deets[1]))	# percentage
	temp.append(stu_deets[2])	# choice 1
	temp.append(stu_deets[3])	# choice 2
	temp.append(stu_deets[4])	# choice 3
	student_details.append(temp)
student_details =  sorted(student_details, key=lambda x:x[1], reverse=True)
for i in range(num_of_students):
	if i < num_of_students - 2:
			if student_details[i][1] == student_details[i+1][1]:
				if student_details[i][0] > student_details[i+1][0]:
					temp = student_details[i][0]
					student_details[i][0] = student_details[i+1][0]
					student_details[i+1][0] = temp
				else:
					continue
print(student_details)
student_seats = []
for i, sub_array in enumerate(student_details):
	if num_of_seats[sub_array[2]] != 0:
		num_of_seats[sub_array[2]] -= 1
		student_seats.append([f'Student-{sub_array[0]}', sub_array[2]])
	elif num_of_seats[sub_array[3]] != 0:
		num_of_seats[sub_array[3]] -= 1	
		student_seats.append([f'Student-{sub_array[0]}', sub_array[3]])
	elif num_of_seats[sub_array[4]] != 0:
		num_of_seats[sub_array[4]] -= 1
		student_seats.append([f'Student-{sub_array[0]}', sub_array[4]])

for ele in student_seats:
	print(ele[0], ele[1])