import os
import difflib
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_awake import keep_alive
import requests
import time
import random

TOKEN = "Enter TOKEN Here"

cid = "Enter channel id without quotes"
#example: cid = 8778172817281

req = requests.get("https://discord.com/api/path/to/the/endpoint%22)

print(req)

gg = open('caught.txt', 'a')
bot = commands.Bot(command_prefix='.')
bot._skip_check = lambda x, y: False

@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = bot.get_channel(cid)
  if text_channel != None:
    list = ['Frysky God','DudeFromMars God','Bui God','Oh My Me','GalFromVenus','Subscribe Frysky on Youtube','Join Yveltal Faction','https://discord.gg/2vGnFbXYFd']
    await text_channel.send(random.choice(list))
    intervals = [1,1.2,1.3]
    await asyncio.sleep(random.choice(intervals))

spammer.start()

@bot.event
async def on_message(message):
      def check(m):
          return m.channel == message.channel  and (("start" in m.content) or ("stop" in m.content))
      msg = message.content # return msg content
      if "start" in msg:
        spammer.start()
      if "stop" in msg:
        spammer.stop()
      while True:
          response = await bot.wait_for('message', check = check, timeout=300) 
          if "The pokémon is" in response.content:
            break

@bot.command()
async def say(ctx, *, args):

  await ctx.send(args)

keep_alive()
bot.run(TOKEN,bot=False)
