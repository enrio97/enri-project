import discord
from discord import colour #모듈 불러오기
token = "OTA5NzA5ODYyNjU5ODE3NTAy.YZIPVA.1r8zEC8uAO3JJPabXOJWqM50Jdw" #봇 토큰 설정하기
client = discord.Client() #client 설정하기

@client.event
async def on_ready(): #봇이 준비되었을 때
    print("봇 준비 완료!")
    print(client.user)
    print("=============")

@client.event
async def on_message(message): #사용자가 메세지를 입력했을때
    if message.content == "야": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("왜") #봇이 "왜"라고 답한다

    
    if message.content == "1+1=": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("3") #봇이 "왜"라고 답한다
    

    if message.content == "인호야 로아 그만해": 
        await message.channel.send("아냐 계속할거야")

    if message.content == "임베드내놔":
        embed = discord.Embed(colour=discord.Colour.red(), title="제-목", description="설-명")
        embed.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/9976D23359F31E3903")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd_5_4NAgI109v6SKDQ6bH4AZyabMKfb-vqQ&usqp=CAU")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="필드 제목", value="필드 설명", inline=False)  #inline이 False라면 다음줄로 넘깁니다.
        await message.channel.send(embed=embed) 

    if message.content.startswith(f"!채널메세지"): #!채널메세지 <채널 아이디> <메세지 내용>
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    
client.run(token)
