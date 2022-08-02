import json

data = """ {
	"name" : "Jinu",
	"phone" : {
		"type" : "int1",
		"number" : "788 952 7828"
	},
	"email" : {
		"hide" : "yes"
	}
} """

info = json.loads(data)		# loads == load S, meaning load from string
print(f'Name: {info["name"]}')
print(f'Phone: {info["phone"]["number"]}')
print(f'Email.hide: {info["email"]["hide"]}')