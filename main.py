import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from functions import *

client = commands.Bot(intents=discord.Intents.all(),
	command_prefix='!',
	help_command=None)


regions = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33', 'P34', 'P35', 'P36', 'P37', 'P38', 'P39', 'P40', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 'F32', 'F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F39', 'F40', 'F41', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'H26', 'H27', 'H28', 'H29', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'H36', 'H37', 'H38', 'H39', 'H40', 'H41', 'H2', 'H3', 'H44', 'H45', 'H46', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S21', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55', 'S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15']
buildings={'farm': {'price': (3, 6)}, 'market': {'price': (3, 6)}, 'fishery': {'price': (5, 10)}, 'harbour': {'price': (5, 10)}, 'mine': {'price': (5, 0)}, 'library': {'price': (10, 0)}, 'school': {'price': (20, 0)}, 'university': {'price': (40, 0)}, 'settlement': {'price': (30, 0)}, 'town': {'price': (50, 0)}, 'city': {'price': (70, 0)}, 'metropolis': {'price': (100, 0)}, 'village': {'price': (10, 0)}, 'Market Town': {'price': (15, 0)}, 'parliament': {'price': (20, 0)}}


config=load_config()

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
		return
	# checking the price of the building after we make sure it exists
	price=buildings[building]['price'][0] 

	if price>available_gold:
		await ctx.reply("no enough gold", mention_author=False)
		return
	if region not in database[player]['regions']:
		await ctx.reply("you dont own that region", mention_author=False)
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
		return
	price=buildings[building]['price'][1] # checking the price of the building after we make sure it exists

	if price>available_gold:
		await ctx.reply("no enough gold", mention_author = False)
		return
	if region not in database[player]['regions']:
		await ctx.reply("you dont own that region", mention_author = False)
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
	final_msg=f"**{player}**\n\n"
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
		finnal_txt += f"**{player}** \n**Gold:** {gold}\n**Food:** {food}\n"
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

load_dotenv()

my_secret=str(os.getenv('discord_token'))
client.run(my_secret)