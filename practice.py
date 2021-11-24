import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다:  ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)

bot.run('OTExNjA5NTIwNTM3NjA4MjUy.YZj4hg.drKSNq5wheh-ZltE-1veXgUY0Eg')