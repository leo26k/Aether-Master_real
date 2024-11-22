import json


players=['test_player_1', 'test_player_2', 'test_player_3', 'test_player_4', 'test_player_5']

def load_config():
	with open('config.json', 'r') as openfile:
	# Reading from json file
		json_object = json.load(openfile)
		openfile.close()
	return json_object


def check_roles(ctx, config):
	returning=[False, False, None]
	for r in ctx.author.roles:
		if str(r).lower() == config['game_master_role']:
			returning[0]=True
		elif str(r).lower() == config['player_role']:
			returning[1]=True
		elif str(r).lower() in config['all_player_roles']:
			returning[2]=str(r).lower()
	print(returning)
	return returning


def read_db():
	# with open('players.json', 'r') as openfile:
	# # Reading from json file
	# 	json_object = json.load(openfile)
	# 	openfile.close()
	database = db
	return database

def write_db(database):
	with open('players.json', 'w') as openfile:
		# database=json.dumps(database, indent=4)
		# openfile.write(database)
		# openfile.close()
		db = database


def print_db():
	database = db
	with open('players.json', 'w') as openfile:
		database=json.dumps(database, indent=4)
		openfile.write(database)
		openfile.close()