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
    msg = message.channel.history(limit=5)
    if msg.content == 'stop' or 'st':
      spammer.stop()
    intervals = [1, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.8, 1.9]
    await asyncio.sleep(random.choice(intervals))

msg = message.channel.history(limit=5)
if msg.content == 'start' or 'run' or 'r':
  spammer.start()

spammer.start()
keep_alive()
bot.run(TOKEN,bot=False)
