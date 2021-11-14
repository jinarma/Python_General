import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

count_teams = int(input('How many teams: '))
total_player_dict = {1:10.5, 2:9.5, 3:9.0, 4:8.5, 5:9.0, 6:9.0, 7:8.5, 8:8.5, 9:8.5, 10:8.5, 11:8.5, 12:10.0, 13:9.0, 14:8.5, 15:8.5, 16:9.0, 17:9.0, 18:9.0, 19:8.5, 20:8.5, 21:8.5, 22:8.5, 23:8.5}

total_player_dict_name = {1:'Jos Butler', 2:'J Bairstow', 3:'K Perera', 4:'D Chandimal', 5:'J Roy', 6:'C Asalanka', 7:'E Morgon', 8:'B Rajapaksa', 9:'D Malan', 10:'A Fernando', 11:'P Nissanka', 12:'W Hasarnaga', 13:'Moin Ali', 14:'D Sonaka', 15:'L Livingstone', 16:'A Rashid', 17:'C Woaks', 18:'M Theekshana', 19:'D Chameera', 20:'C Jordon', 21:'T Mills', 22:'L Kumara', 23:'C Karunaratna'}

for i in range(0,count_teams*2,2):
	sum = 0
	player_list = []
	for j in range(12):
		while True:
			temp = int(input(j+1))
			if temp not in player_list:
				if j <= 10:
					sheet1.write(j, i, total_player_dict_name[temp])
					sheet1.write(j, i+1, total_player_dict[temp])
					sum = sum + total_player_dict[temp]
				else:
					sheet1.write(j, i, total_player_dict_name[temp])
					sheet1.write(j, i+1, total_player_dict[temp])
					sum = sum + total_player_dict[temp]
					sheet1.write(j+1, i+1, sum)
				player_list.append(temp)
				break
			else:
				print('Player already exists, try again')
				continue
		

wb.save('D:\Programming\Python\Github\Python_General\Dream 11 2.0\player test.xls')

