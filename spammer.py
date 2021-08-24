import os
import difflib
import sqlite3
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_awake import keep_alive
import requests
from discord_webhook import DiscordWebhook
import time
import random

TOKEN = "ODQxMzQ4NTIyNTMxNDg3Nzc0.YSTUVA.RmhW81V2ZVmbjfddL4hg6_3I87g"

cid = 879676296513335326
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
    list = ['Frysky God','DudeFromMars God','OG Developers','Subscribe Frysky on Youtube','Join Yveltal Faction','https://discord.gg/2vGnFbXYFd']
    await text_channel.send(random.choice(list))
    intervals = [1,1.2,1.3]
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

keep_alive()
bot.run(TOKEN,bot=False)
