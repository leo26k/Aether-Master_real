import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from functions import *
from keep_alive import keep_alive

client = commands.Bot(intents=discord.Intents.all(),
	command_prefix='!',
	help_command=None)


regions = ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21', 'O22', 'O23', 'O24', 'O25', 'O26', 'O27', 'O28', 'O29', 'O30', 'O31', 'O32', 'O33', 'O34', 'O35', 'O36', 'O37', 'O38', 'O39', 'O40', 'O41', 'O42', 'O43', 'O44', 'O45', 'O46', 'O47', 'O48', 'O49', 'O50', 'O51', 'O52', 'O53', 'O54', 'O55', 'O56', 'O57', 'O58', 'O59', 'O60', 'O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'O71', 'O72', 'O73', 'O74', 'O75', 'O76', 'O77’ ‘O78', 'O79', 'O80', 'O81', 'O82', 'O83', 'O84', 'O85', 'O86', 'O87', 'O88', 'O89', 'O90', 'O91', 'O92', 'O93', 'O94', 'O95', 'O96', 'O97', 'O98', 'O99', 'O100', 'O101', 'O102', 'O103', 'O104', 'O105', 'O106', 'O107', 'O108', 'O109', 'O110', 'O111', 'O112', 'O113', 'O114', 'O115', 'O116', 'O117', 'O118', 'O119', 'O120', 'O121', 'O122', 'O123', 'O124', 'O125', 'O126', 'O127', 'O128', 'O129', 'O130’ ‘O131', 'O132', 'O133', 'O134', 'O135', 'O136', 'O137', 'O138', 'O139', 'O140', 'O141', 'O142', 'O143', 'O144', 'O145', 'O146', 'O147', 'O148', 'O149', 'O150', 'O151', 'O152', 'O153', 'O154', 'O155', 'O156', 'O157', 'O158', 'O159', 'O160', 'O161', 'O162', 'O163', 'O164', 'O165', 'O166', 'O167', 'O168', 'O169', 'O170', 'O171', 'O172', 'O173', 'O174', 'O175', 'O176', 'O178', 'O179', 'O180', 'O181', 'O182', 'O183', 'O184', 'O185', 'O186', 'O187', 'O188', 'O189', 'O190', 'O191', 'O192', 'O193', 'O194', 'O195', 'O196', 'O197', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22', 'T23', 'T24', 'T25', 'T26', 'T27', 'T28', 'T29', 'T30', 'T31', 'T32', 'T33', 'T34', 'T35', 'T36', 'T37', 'T38', 'T39', 'T40', 'T41', 'T42', 'T43', 'T44', 'T45', 'T46', 'T47', 'T48', 'T49', 'T50', 'T51', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', '‘H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'H26', 'H27', 'H28', 'H29', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'H36', 'H37', 'H38', 'H39', 'H40', 'H41', 'H42', 'H43', 'H44', 'H45', 'H46', 'H47', 'H48', 'H49', 'H50', 'H51', 'H52', 'H53', 'H54', 'H55', 'H56', 'H57', 'H58', 'H59', 'H60', 'H61', 'H62', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33', 'P34', 'P35', 'P36', 'P37', 'P38', 'P39', 'P40', 'P41', 'P42', 'P43', 'P44', 'P45', 'P46', 'P47', 'P48', 'P49', 'P50', 'P51', 'P52', 'P53', 'P54', 'P55', 'P56', 'P57', 'P58', 'P59', 'P60', 'P61', 'P62', 'P63', 'P64', 'P65', 'P66', 'P67', 'P68', 'P69', 'P70', 'P71', 'P72', 'P73', 'P74', 'P75', 'P76', 'P77’ ‘P78', 'P79', 'P80', 'P81', 'P82', 'P83', 'P84', 'P85', 'P86', 'P87', 'P88', 'P89', 'P90', 'P91', 'P92', 'P93', 'P94', 'P95', 'P96', 'P97', 'P98', 'P99', 'P100', 'P101', 'P102', 'P103', 'P104', 'P105', 'P106', 'P107', 'P108', 'P109', 'P110', 'P111', 'P112', 'P113', 'P114', 'P115', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 'F32', 'F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F39', 'F40', 'F41', 'F42', 'F43', 'F44', 'F45', 'F46', 'F47', 'F48', 'F49', 'F50', 'F51', 'F52', 'F53', 'F54', 'F55', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55', 'S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20', 'J21', 'J22', 'J23', 'J24', 'J25', 'J26', 'J27', 'J28', 'J29', 'J30', 'J31', 'J32', 'J33', 'J34', 'J35', 'J36', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D40', 'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D47', 'D48', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48']
buildings={'farm': {'price': (3, 6)}, 'market': {'price': (3, 6)}, 'fishery': {'price': (5, 10)}, 'harbour': {'price': (5, 10)}, 'mine': {'price': (5, 0)}, 'library': {'price': (10, 0)}, 'school': {'price': (20, 0)}, 'university': {'price': (40, 0)}, 'settlement': {'price': (30, 0)}, 'town': {'price': (50, 0)}, 'city': {'price': (70, 0)}, 'metropolis': {'price': (100, 0)}, 'village': {'price': (10, 0)}, 'Market Town': {'price': (15, 0)}, 'parliament': {'price': (20, 0)}}




config=load_config()




###################################    TRIVIAL CODE HERE  #####################################

# for player in config['all_player_roles']:
# 	db[player] = {
# 		'gold': 0,
# 		'food': 0,
# 		'pop': 0,
# 		'ore': 0,
# 		'aether': 0,
# 		'mythical': 0,
# 		'regions': [],
# 		'orders': [],
# 		'buildings': {}
# 	}



# db['test_player_1']['regions'].append('P1')


####################################################################################################

@client.event
async def on_ready():
	print('online')


@client.command()
async def test(ctx):
	await ctx.channel.send('test')

@client.command()
async def build(ctx, building, region):

	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0] and not roles[1]:
		return
	player=roles[2]

	# get the required data
	database=read_db()
	region=region.upper()
	building=building.lower()
	available_gold=database[player]['gold']

	# check if the command is possible
	if building not in buildings:
		await ctx.reply(f"{building} doesnt exist", mention_author=False)
		await ctx.message.add_reaction('❌')
		return
	# checking the price of the building after we make sure it exists
	price=buildings[building]['price'][0] 

	if price>available_gold:
		await ctx.reply("no enough gold", mention_author=False)
		await ctx.message.add_reaction('❌')
		return
	if region not in database[player]['regions']:
		await ctx.reply("you dont own that region", mention_author=False)
		await ctx.message.add_reaction('❌')
		return
	
	# do the command and write to database
	database[player]['gold'] -= price
	database[player]['orders'].append({'type': "build", 'region': region, 'building': building})
	write_db(database)
	await ctx.message.add_reaction('👍')


@client.command()
async def upgrade(ctx, building, region):

	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0] and not roles[1]:
		return
	player=roles[2]

	# get the required data
	database=read_db()
	region=region.upper()
	building=building.lower()
	available_gold=database[player]['gold']

	# check if the command is possible
	if building not in buildings:
		await ctx.reply(f"{building} doesnt exist", mention_author = False)
		await ctx.message.add_reaction('❌')
		return
	price=buildings[building]['price'][1] # checking the price of the building after we make sure it exists

	if price>available_gold:
		await ctx.reply("no enough gold", mention_author = False)
		await ctx.message.add_reaction('❌')
		return
	if region not in database[player]['regions']:
		await ctx.reply("you dont own that region", mention_author = False)
		await ctx.message.add_reaction('❌')
		return
	
	# do the command and write to database
	database[player]['gold'] -= price
	database[player]['orders'].append({'type': "upgrade", "region": region, "building": building})
	write_db(database)
	await ctx.message.add_reaction('👍')

@client.command()
async def stats(ctx):
	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0] and not roles[1]:
		return
	player=roles[2]

	# get the required data
	database=read_db()

	# make a stats message
	final_msg=f"**{player}**     <:{config['player_flags'][player]['emoji_name']}:{config['player_flags'][player]['emoji_id']}> \n\n"
	gold=database[player]['gold']
	food=database[player]['food']
	pop=database[player]['pop']
	ore=database[player]['ore']
	aether=database[player]['aether']
	mythical=database[player]['mythical']
	regions=', '.join(database[player]['regions'])
	# units=', '.join(database[player]['units'])
	# orders_text=
	n = 1
	orders_txt = ""
	for order in database[player]['orders']:
		if order['type'] in ['upgrade', 'build']:
			orders_txt += f"{n}.   {order['type']} **{order['building']}** in **{order['region']}**\n"
		elif order['type'] in ['attack', 'move']:
			orders_txt += f"{n}.  **{order['type']}** {order['text']}\n"
		n += 1
	final_msg+=f"**Gold:** {gold}\n**Food:** {food}\n**Pop:** {pop}\n**Ore:** {ore}\n**Aether:** {aether}\n**Mythical:** {mythical}\n**Regions:** {regions}\n**Orders:\n** {orders_txt}"	
	await ctx.reply(final_msg, mention_author=False)
	return


@client.command()
async def remove(ctx, index = 0):
	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0] and not roles[1]:
		return
	player=roles[2]

	# get the required data
	database=read_db()
	removed_orders = []
	if index == -1:		
		for _ in range(len(database[player]['orders'])):
			removed_order = database[player]['orders'].pop(-1)
			removed_orders.append(removed_order)
	else:
		removed_order = database[player]['orders'].pop(index - 1)
		removed_orders.append(removed_order)
	for order in removed_orders:
		order_type = order['type']
		if order_type == 'build':
			database[player]['gold'] += buildings[order['building']]['price'][0]
		elif order_type == 'upgrade':
			database[player]['gold'] += buildings[order['building']]['price'][1]

	
	write_db(database)
	await ctx.message.add_reaction('👍')
	return 

@client.command()
async def new_turn(ctx, turn):
	# verify the GM
	roles=check_roles(ctx, config)
	if not roles[0]:
		return
	# get the required data	
	database=read_db()

	finnal_txt = f"**TURN {turn} RESULTS** \n\n"
	for player in database:
		gold = database[player]['gold']
		food = database[player]['food']
		finnal_txt += f"**{player}**     <:{config['player_flags'][player]['emoji_name']}:{config['player_flags'][player]['emoji_id']}>\n**Gold:** {gold}\n**Food:** {food}\n"
		n = 1
		
		orders_txt = "**Orders:** \n"
		sorted_orders = []
		order_types = ['build', 'upgrade', 'move', 'attack']
		for type in order_types:
			for order in database[player]['orders']:
				if type == order['type']:
					sorted_orders.append(order)
		for order in sorted_orders:
			if order['type'] in ['upgrade', 'build']:
				orders_txt += f"{n}.   {order['type']} **{order['building']}** in **{order['region']}** \n"
			if order['type'] in ['attack', 'move']:
				orders_txt += f"{n}.   **{order['type']}** {order['text']} \n"
			n += 1
		finnal_txt += f"{orders_txt}\n\n"
	await ctx.channel.send(finnal_txt)


@client.command()
async def give(ctx, amount, resource, player):
	# verify the GM
	roles=check_roles(ctx, config)
	if not roles[0]:
		return
	# get the required data
	database=read_db()

	resource = resource.lower()
	if resource not in database[player]:
		await ctx.reply("wrong resource", mention_author = False)
	database[player][resource] += int(amount)
	write_db(database)
	await ctx.message.add_reaction('👍')
	return

@client.command()
async def change(ctx, region, player_1, player_2):
	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0]:
		return
	# get the required data
	database=read_db()

	region = region.upper()
	database[player_1]['regions'].remove(region)
	database[player_2]['regions'].append(region)
	write_db(database)
	await ctx.message.add_reaction('👍')
	return

@client.command()
async def move(ctx, *args):
	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0] and not roles[1]:
		return
	# get the required data
	player = roles[2]
	database=read_db()

	print(args)
	database[player]['orders'].append({'type': 'move', 'text': " ".join(list(args))})
	write_db(database)
	await ctx.message.add_reaction('👍')
	return

@client.command()
async def attack(ctx, *args):
	# verify the player
	roles=check_roles(ctx, config)
	if not roles[0] and not roles[1]:
		return
	# get the required data
	player = roles[2]
	database=read_db()

	print(args)
	database[player]['orders'].append({'type': 'attack', 'text': " ".join(list(args))})
	write_db(database)
	await ctx.message.add_reaction('👍')
	return

# load_dotenv()

# my_secret=str(os.getenv('discord_token'))

# @client.command()
# async def get_db(ctx):
# 	print_db()

keep_alive()
# my_secret = str(os.environ['discord_token'])
load_dotenv()

my_secret=str(os.getenv('discord_token'))
client.run(my_secret)
