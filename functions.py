import json


players=['test_player_1', 'test_player_2', 'test_player_3', 'test_player_4', 'test_player_5']

def check_roles(ctx):
	returning=[False, False, None]
	for r in ctx.author.roles:
		if str(r).lower() == 'game master man':
			returning[0]=True
		elif str(r).lower() == 'player':
			returning[1]=True
		elif str(r).lower() in players:
			returning[2]=str(r).lower()
	print(returning)
	return returning


def read_db():
	with open('players.json', 'r') as openfile:
	# Reading from json file
		json_object = json.load(openfile)
		openfile.close()
	return json_object

def write_db(db):
	with open('players.json', 'w') as openfile:
		db=json.dumps(db, indent=4)
		openfile.write(db)
		openfile.close()
