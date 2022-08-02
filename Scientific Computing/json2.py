import json

inp = """ [
	{
		"id" : "001",
		"x"	: "2",
		"name" : "Jinu"
	},
	{
		"id" : "009",
		"x" : "7",
		"name" : "Shubhankar"
	}
] """

info = json.loads(inp)
for i, ele in enumerate(info):
	print(f'Name({i}): {info[i]["name"]}')
	print(f'Id({i}): {info[i]["id"]}')
	print(f'Attribute({i}): {info[i]["x"]}')