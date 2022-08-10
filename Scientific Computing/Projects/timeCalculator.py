def add_time(start, duration, day=None):
	start = start.split()
	start_minutes = start[0].split(':')
	start_minutes = int(start_minutes[0])*60+int(start_minutes[1])
	if start[1].casefold() == 'pm':
		start_minutes += 720

	duration_minutes = duration.split(':')
	duration_minutes = int(duration_minutes[0])*60+int(duration_minutes[1])
	new_time = start_minutes+duration_minutes
	new_hours = (new_time//60)
	new_minutes = new_time%60
	total_days = new_hours//24
	if new_hours%12 == 0:
		new_hours_string = str('12')
	else:
		new_hours_string = str(new_hours%12)
	if new_minutes < 10:
		new_minutes_string = '0'+str(new_minutes)
	else:
		new_minutes_string = str(new_minutes)
	if day == None:
		if new_hours%24 >= 12:
			if total_days == 0:
				new_time = f'{new_hours_string}:{new_minutes_string} PM'
			elif total_days == 1:
				new_time = f'{new_hours_string}:{new_minutes_string} PM (next day)'
			elif total_days > 1:
				new_time = f'{new_hours_string}:{new_minutes_string} PM ({total_days} days later)'
		else:
			if total_days == 0:
				new_time = f'{new_hours_string}:{new_minutes_string} AM'
			elif total_days == 1:
				new_time = f'{new_hours_string}:{new_minutes_string} AM (next day)'
			elif total_days > 1:
				new_time = f'{new_hours_string}:{new_minutes_string} AM ({total_days} days later)'
	elif day != None:
		week = {
			0:'sunday',
			1:'monday',
			2:'tuesday',
			3:'wednesday',
			4:'thursday',
			5:'friday',
			6:'saturday'
			}
		temp_total_days = 0
		temp_total_days += list(week.values()).index(day.casefold())
		temp_total_days += total_days
		temp_total_days %= 7
		day = week[temp_total_days]
		if new_hours % 24 >= 12:
			if total_days == 0:
				new_time = f'{new_hours_string}:{new_minutes_string} PM, {day.capitalize()}'
			elif total_days == 1:
				new_time = f'{new_hours_string}:{new_minutes_string} PM, {day.capitalize()} (next day)'
			elif total_days > 1:
				new_time = f'{new_hours_string}:{new_minutes_string} PM, {day.capitalize()} ({total_days} days later)'
		else:
			if total_days == 0:
				new_time = f'{new_hours_string}:{new_minutes_string} AM, {day.capitalize()}'
			elif total_days == 1:
				new_time = f'{new_hours_string}:{new_minutes_string} AM, {day.capitalize()} (next day)'
			elif total_days > 1:
				new_time = f'{new_hours_string}:{new_minutes_string} AM, {day.capitalize()} ({total_days} days later)'

	return new_time


print(add_time("11:59 PM", "24:05", "Wednesday"))
