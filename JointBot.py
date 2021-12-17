
import os
import difflib
import sqlite3
#db = sqlite3.connect('poke2auto.db')
#cur = db.cursor()
count = 0
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
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook
TOKEN = "Enter bot TOKEN"
cid = Enter cid
#example: cid = 8778172817281
#Don't put quots around channel ID
editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)
import time
#mon_url=input('url')
gg = open('caught.txt', 'a')
import random
#cid = 801907193754288249
client = commands.Bot(command_prefix='.')
client._skip_check = lambda x, y: False

@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = client.get_channel(cid)
  if text_channel != None:
    list = [i for i in range(1,100000)]
    await text_channel.send(random.choice(list))
    intervals = [2,3,4]
    await asyncio.sleep(random.choice(intervals))

spammer.start()

hint = ""
@client.event
async def on_message(message):
      
      
      def check(m):
        return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content
      msg = message.content # return msg content
      if "start" in msg:
        spammer.start()
      if "stop" in msg:
        spammer.stop()

      global hint
      embeds = message.embeds # return list of embeds
      if not message.embeds:
        await client.process_commands(message)
        return
      title = (embeds[0].to_dict()['title'])   
      if "pokémon has appeared" in title:
        hint = ""
        time.sleep(1)
        m = await message.channel.send(".hint")
        
        while True:
          response = await client.wait_for('message', check = check, timeout=300) 
          if "The pokémon is" in response.content:
            break
        time.sleep(1)
      s = response.content.split(" is ")[1].replace(".","")
      print(s)
      x = get_mon(s)
      #print(options)
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
