import discord
import random

client = discord.Client()

answers = [
	'Hey there!',
	'OwO Hewwo, theya!',
	'Hi',
	'Hello!',
	'Sup',
	'Bonjour',
	"What's up?"
]

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send(answers[random.randint(0, 6)])

@client.event
async def on_member_join(member):
	for channel in member.server.channels:
		if str(channel) == 'welcome':
			await client.send_message(f"Welcome to the server {member.mention}!" + 
				" Talk in #general")

client.run('token')