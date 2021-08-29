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

f = open('pokes.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
mon_list = []
for i in file:
    if len(i) >= 3:
        mon_list.append(i)

TOKEN = "ENTER YOUR TOKEN HERE"
cid = "Enter CID without quotes"
#example: cid = 8778172817281
#Don't put quotes around channel ID

req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)

gg = open('caught.txt', 'a')

client = commands.Bot(command_prefix='.')
client._skip_check = lambda x, y: False

@tasks.loop(seconds=14400)
async def sleeper():
  time.sleep(seconds = 1)

hint = ""
@client.event
async def on_message(message):
      
      
      def check(m):
          return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content

      global hint

   
    #if "The pokémon is" in message.content:
      #await message.delete()
      embeds = message.embeds # return list of embeds
    #print("tes")
      if not message.embeds:
        await client.process_commands(message)
        return
      title = (embeds[0].to_dict()['title'])
    #print(title)
   
      if "pokémon has appeared" in title:
        hint = ""
        time.sleep(0.75)
        m = await message.channel.send(".hint")
        
        while True:
          response = await client.wait_for('message', check = check, timeout=300) 
          if "The pokémon is" in response.content:
            break
        time.sleep(1)
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
        #print(val)
  length = len(val)
  l = list(val)
  new_chars = []
  
  
  with open('pokes.txt') as f:
       lines = [line.rstrip() for line in f]
  new_names = []
  for i in lines:
    if len(i) == length:
      new_names.append(i)
  #print(new_names)
  final_list = []
  for i in new_names:
    name_list = list(i)
    index = 0
    #print(i)

    flag = False
    for k in l:
      if name_list[index] != k and k != "-":
       # print(name_list[index]+"!="+k)
        flag = True
      index = index+1
    if not flag:
      final_list.append(i)
  #print(final_list)
  return final_list

@client.command()
async def say(ctx, *, args):
  await ctx.send(args)

keep_alive()
client.run(TOKEN,bot=False)