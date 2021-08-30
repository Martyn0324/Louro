import discord
from discord.ext import commands
import random
import asyncio
import time
import re
import numpy
import matplotlib.pyplot as plt
from nltk import word_tokenize

token = open("C:/Program Files (x86)/Steam/Músicas/tokenLouro.txt", 'r').readline()
client = commands.Bot(command_prefix = 'Louro, ', case_insensitive=True)

@client.remove_command('help')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_author(name='List of commands')
    embed.set_thumbnail(url="https://i.pinimg.com/564x/57/76/5a/57765aba9774ab053136897846feb25c.jpg")
    embed.add_field(name='Louro, hello', value='Test command, used to check if bot is working', inline=False)
    embed.add_field(name='Louro, d6', value='Dice command, this one returns a number from 1 to 6', inline=False)
    embed.add_field(name='Louro, d20', value='Dice command, this one returns a number from 1 to 20', inline=False)
    embed.add_field(name='Louro, duel', value="Minigame command. Use it to solve your problems with someone", inline=False)
    embed.add_field(name='Louro, birb', value="Birddies, birddies everywhere. Birddies are cute, and if you disagree, you're wrong", inline=False)
    embed.add_field(name='Louro, anime', value="Try it, weeb!", inline=False)
    embed.add_field(name="There's also other commands that aren't included here. They're secrets. Crááá!", value="Try finding something...", inline=False)
    await ctx.send(embed=embed)

#Testing reaction to commands and checking if the bot is working
@client.command()
async def hello(ctx):
    response = "Hello!"
    await ctx.send(response)

#Testing how to send emojis using bot
@client.command()
async def emoji(ctx):
    emoji = ['<:shocked:768832734625267743>', '<:wtf:768834966695444550>', '<:screaming:768835859394723881>', '<:saywhat:768835998037573702>',
    '<:happy:768836056245731359>', '<:badass:768835911685242930>']
    await ctx.send(random.choice(emoji))
    for i in random.sample(emoji, 5):
        await ctx.send(i)

#Testing Regular Expression
@client.listen()
async def on_message(message):
    if message.content.lower() == 'louro, are you ok?':
        tokenization = re.split(r"[.?!]", message.content)
        await message.channel.send(tokenization)
        response = "Yes, why do you bother?"
        await message.channel.send(response)

@client.listen()
async def on_message(message):
    if message.content.lower() == 'louro, tokenize this!':
        tokenization = word_tokenize(message.content)
        await message.channel.send(tokenization)
        response = "There it is. Are you happy now? Cráááá!"
        await message.channel.send(response)        
        
#Changing status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Type 'Louro, help' for help command"))

#Testing edit messages resource
@client.command()
async def edit(ctx):
    await ctx.send("Ok. Let's do this")
    msg = await ctx.send('1')
    await asyncio.sleep(1.0)
    await msg.edit(content='2')
    time.sleep(1)
    await msg.edit(content='3')
    await msg.add_reaction(':gunparrot:769189863890485289')
