import os
import difflib
import sqlite3
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook
import time
import random


count = 0
f = open('pokemon.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
pokemon_list = []
for i in file:
    if len(i) >= 3:
        pokemon_list.append(i)

TOKEN = "token here"
cid = "channel id here"
#example: cid = 8778172817281
#Don't put quots around channel ID

req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)

gg = open('caught.txt', 'a')
bot = commands.Bot(command_prefix='.')
bot._skip_check = lambda x, y: False

@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = bot.get_channel(cid)
  if text_channel != None:
    list = ['Frysky God','DudeFromMars God','OG Developers','Subscribe Frysky on Youtube','Join Yveltal Faction']
    await text_channel.send(random.choice(list))
    intervals = [1, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.8, 1.9]
    await asyncio.sleep(random.choice(intervals))

@tasks.loop(seconds = 0.2)
async def sleeper():
  await text_channel.send('Sleeping for 60 seconds')
  time.sleep(seconds = 60)
  spammer.start()

spammer.start()

@bot.command()
async def stop(ctx):
    spammer.stop()

@bot.command()
async def spam(ctx):
  spammer.start()
  
@bot.command()
async def say(ctx, *, args):
  
  await ctx.send(args)

keep_awake()
bot.run(TOKEN,bot=False)