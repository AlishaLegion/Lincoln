import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import json
Bot = commands.Bot(command_prefix="*")

@Bot.event
async def on_message(message):
    with open('C:\\Users\\ALISHKA\\Desktop\\hard\\lvl.json', 'r') as f:
        users = json.load(f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]['exp'] = 0
            users[user]['lvl'] = 1
    async def add_exp(users,user,exp):
        users[user]['exp'] += exp
    async def add_lvl(users,user):
        exp = users[user]['exp']
        lvl = users[user]['lvl']
        if exp > lvl:
            await message.channel.send(f'{message.author.mention} **повысил свой уровень!**')
            users[user]['exp'] = 0
            users[user]['lvl'] = lvl + 1
    await update_data(users,str(message.author.id))
    await add_exp(users,str(message.author.id), 0.1)
    await add_lvl(users,str(message.author.id))
    with open('C:\\Users\\ALISHKA\\Desktop\\hard\\lvl.json', 'w') as f:
        json.dump(users,f)
        
@Bot.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 820346016317833236:
        for guild in Bot.guilds:
            maincategory = discord.utils.get(guild.categories, id=820345850772455474)
            channel2 = await guild.create_voice_channel(name=f'{member.display_name}',category = maincategory)
            await channel2.set_permissions(member,connect=True,mute_members=True,move_members=True,manage_channels=True)
            await member.move_to(channel2)
            def check(x,y,z):
                return len(channel2.members) == 0
            await Bot.wait_for('voice_state_update',check=check)
            await channel2.delete()

Bot.run('ODE1MjYzMTcyNTYyOTExMjcx.YDp2_w.PXbKA5tnL0z0wBQRdV0kpkecA-I')