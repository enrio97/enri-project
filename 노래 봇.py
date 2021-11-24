#1서버에 봇 추가하기---------------------------------------------------------------------------------------------------------------------------------------------------------------

import asyncio
import discord
from discord import voice_client
from discord.colour import Color
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
    await ctx.send(embed= discord.Embed(title= '따라하기', description = text, color = 0x00ff00))

bot.run('OTExNjA5NTIwNTM3NjA4MjUy.YZj4hg.drKSNq5wheh-ZltE-1veXgUY0Eg')

#2봇 온라인으로 바꾸고 명령어 넣어주기--------------------------------------------------------------------------------------------------------------------------------------------------------------
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다:  ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 들어와(ctx):
    global vc
    vc = await ctx.message.author.voice.channel.connect()

bot.run('OTExNjA5NTIwNTM3NjA4MjUy.YZj4hg.drKSNq5wheh-ZltE-1veXgUY0Eg')

#2봇을 음성채널에 들어오게 만들기--------------------------------------------------------------------------------------------------------------------------------------------------------------