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

f = open('pokes.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
pokemons = []
for i in file:
    if len(i) >= 3:
        pokemons.append(i)

req = requests.get("https://discord.com/api/path/to/the/endpoint")

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

hint = ""
@bot.event
async def on_message(message):
        
      def check(m):
          return m.channel == message.channel and m.author != bot.user and "The pokémon is" in m.content
      global hint
      embeds = message.embeds

      if not message.embeds:
        await bot.process_commands(message)
        return
      
      title = (embeds[0].to_dict()['title'])   
      if "pokémon has appeared" in title:
        hint = ""
        m = await message.channel.send(".hint")
        
        while True:
          response = await bot.wait_for('message', check = check, timeout=300) 
          if "The pokémon is" in response.content:
            break
        
      s = response.content.split(" is ")[1].replace(".","")
      print(s)
      x = get_mon(s)
      print(x)
      first_options = x
      for i in first_options:
        await message.channel.send(".catch "+i)
 
def get_mon(val):
 val = val.lower()
 while "\_" in val:
     val = val.replace("\_", "-")
 length = len(val)
 l = list(val)
 new_chars = []
 with open('pokemon.txt') as f:
     lines = [line.rstrip() for line in f]
 new_names = []
 for i in lines:
   if len(i) == length:
     new_names.append(i)
 final_list = []
 for i in new_names:
   name_list = list(i)
   index = 0
   flag = False
   for k in l:
     if name_list[index] != k and k != "-":
       flag = True
     index = index+1
   if not flag:
     final_list.append(i)
 return final_list

@bot.command()
async def say(ctx, *, args):
  
  await ctx.send(args)

keep_alive()
bot.run(TOKEN,bot=False)
