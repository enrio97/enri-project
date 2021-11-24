import discord
from discord import colour #모듈 불러오기
token = "OTEwMDc1NTc0MDg3NzQxNDcy.YZNj7Q._PyeHtyhi-TsvQPb3q2OB6hEvvg" #봇 토큰 설정하기
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

    if message.content == "인호야 로아 그만해": 
        await message.channel.send("아냐 계속할거야")

    if message.content == "화염의 호흡 제 1형!":
        embed = discord.Embed(colour=discord.Colour.red(), title="렌고쿠 쿄주로", description="염주")
        embed.set_thumbnail(url="https://w.namu.la/s/d10f45a05ee8dbafc1729d19ee3108c296f85c3be509ee11ef3947bb9e2cba3b24b2817276ee8905b10cab5d0266e042bf0341d146126fc0041d09cdc9bf90a236ed760785c670929c35d3244ffec2edcdc875eb72a53d42c947f3492858a83c")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx3DZPJ9H9shpLF-26SYII7UWZYYAjKc-ncw&usqp=CAU")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="화염의 호흡 제 1형", value="시라누이", inline=False)  #inline이 False라면 다음줄로 넘깁니다.
        await message.channel.send(embed=embed) 

    if message.content == "화염의 호흡 제 9형!":
        embed = discord.Embed(colour=discord.Colour.red(), title="렌고쿠 쿄주로", description="염주")
        embed.set_thumbnail(url="https://mblogthumb-phinf.pstatic.net/MjAyMTAyMTNfMTA5/MDAxNjEzMTYxNDU3MTg0.IxFEE3Yr87sKGgvzXc0jv9t7QZEqTqH12dHQfx9FT3Ig.dwsrmPnHcBhyqfXMI6ftyicOyHJ8N6eLLMDtHKPXuh0g.JPEG.sjn1203/20201014%EF%BC%8D00010003%EF%BC%8Dmagmix%EF%BC%8D000%EF%BC%8D8%EF%BC%8Dview.jpg?type=w800")
        embed.set_image(url="https://i.ytimg.com/vi/UPJb4vSlLW0/maxresdefault.jpg")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="화염의 호흡 제 9형", value="연옥", inline=False)  #inline이 False라면 다음줄로 넘깁니다.
        await message.channel.send(embed=embed) 



client.run(token)
