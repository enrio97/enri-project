import discord
import asyncio
from discord import embeds

from discord.colour import Color


client = discord.Client()

token = "OTExNjA5NTIwNTM3NjA4MjUy.YZj4hg.drKSNq5wheh-ZltE-1veXgUY0Eg"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('봇이 활동중에 표시 될 이름')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "엔리":
        await message.channel.send("파이팅!")


    if message.content == "임베드내놔":
        embed = discord.Embed(colour=discord.Colour.red(), title="엔리의 서버", description="봇 개발 열심히하기~")
        embed.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/9976D23359F31E3903")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd_5_4NAgI109v6SKDQ6bH4AZyabMKfb-vqQ&usqp=CAU")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="필드 제목", value="필드 설명", inline=False)  #inline이 False라면 다음줄로 넘깁니다.
        await message.channel.send(embed=embed) 


client.run(token)