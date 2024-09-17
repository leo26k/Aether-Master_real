import json


def check_roles(ctx):
	returning=[False, False, None]
	for r in ctx.author.roles:
		if str(r).lower() == 'gm':
			returning[0]=True
		elif str(r).lower() == 'player':
			returning[1]=True
		elif str(r).lower() in nations['nations']:
			returning[2]=str(r).lower()
	print(returning)
	return returning


def read_db():
	with open('da.json', 'r') as openfile:
	# Reading from json file
		json_object = json.load(openfile)
		openfile.close()
	return json_object
