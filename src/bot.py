import random

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='%')
token = 'token'

@client.event
async def on_ready():
	print("Bot is ready")

@client.command(aliases=['pong'])
async def ping(ctx):
	#Sends user's ping rounded in ms
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
#Take question as full string
async def eBall(ctx, *, question):
	#Total responses
	responses = json.loads(open('8ball.json').read())
	#Send random response
	await ctx.send(f"Q: {question}\nA: {random.choice(responses)}")

@client.command()
#Role can only be used admins
@commands.has_role("admin")
async def clear(ctx, amount=11):
	#Clear x amount of messages, also clears the command message
	await ctx.channel.purge(limit=amount)


#Run bot
client.run(token)