def arithmetic_arranger(problems):
	# print(problems)
	try:
		problems, decision = problems
	except:
		problems = problems[0]
		decision = False

	# print(len(problems))
	if len(problems) > 5:
		return 'Error: Too many problems.'
	top = []
	middle = []
	seperator = []
	bottom = []
	for expression in problems:
		expression = expression.split()

		if expression[1] != '+' and expression[1] != '-':
			return "Error: Operator must be '+' or '-'."

		try:
			if int(expression[0]) > 9999 or int(expression[2]) > 9999:
				return 'Error: Numbers cannot be more than four digits.'

			elif int(expression[0]) >= int(expression[2]):
				line_size = len(expression[0])+2
				seperator.append('-'*line_size)

			elif int(expression[0]) < int(expression[2]):
				line_size = len(expression[2])+2
				seperator.append('-'*line_size)
		except:
			return 'Error: Numbers must only contain digits.'

		top.append(expression[0].rjust(line_size))
		middle.append(expression[1]+expression[2].rjust(line_size-1))

		if decision == True:
			if expression[1] == '+':
				bottom.append(str(int(expression[0])+int(expression[2])).rjust(line_size))

			elif expression[1] == '-':
				bottom.append(str(int(expression[0])-int(expression[2])).rjust(line_size))

	arranged_problems = '    '.join(top)
	arranged_problems += '\n'
	arranged_problems += '    '.join(middle)
	arranged_problems += '\n'
	arranged_problems += '    '.join(seperator)
	if decision == True:
		arranged_problems += '\n'
		arranged_problems += '    '.join(bottom)
	# print(repr(arranged_problems))
	return arranged_problems


print(arithmetic_arranger([['98 + 35', '3801 - 2', '45 + 43', '123 + 49'], True]))
