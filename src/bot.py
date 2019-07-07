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
	responses = [
		"It is certain", 
		"It is decidedly so", 
		"Without a doubt",
	    "Yes, definitely", 
	    "You may rely on it", 
	    "As I see it, yes",
	    "Most likely", 
	    "Outlook good", 
	    "Signs point to yes", 
	    "Yes",
	    "Reply hazy, try again", 
	    "Ask again later",
	    "Better not tell you now", 
	    "Cannot predict now",
	    "Concentrate and ask again", 
	    "Don't bet on it",
	    "My reply is no", 
	    "My sources say no", 
	    "Outlook not so good",
	    "Very doubtful"
	]	
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