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

TOKEN = "token here"
cid = "channel id here without quotes"
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

gg = open('caught.txt', 'a')
client = commands.Bot(command_prefix='.')
client._skip_check = lambda x, y: False

spammer.start()

hint = ""
@client.event
async def on_message(message):
        
      def check(m):
          return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content
      global hint
      embeds = message.embeds

      if not message.embeds:
        await client.process_commands(message)
        return
      
      title = (embeds[0].to_dict()['title'])   
      if "pokémon has appeared" in title:
        hint = ""
        m = await message.channel.send(".hint")
        
        while True:
          response = await client.wait_for('message', check = check, timeout=300) 
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
