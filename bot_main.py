import discord
import os

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print("start")
    game = discord.Game('코펭!!')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if "시발" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "욕 쓰자" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 응~안되~")

    if "욕쓰자" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 응~안되~")

    if "시발" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "씨발" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "tlqkf" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "Tlqkf" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "미친" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "미1친" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㅅ1ㅂ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "시1발" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")



    if "병신" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "지랄" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "존나" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "존1나" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㅈㄴ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㅅㅂ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㄱㅅㄲ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㄳㄲ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㄱㅅㄲ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "개새끼" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㅁㅊ" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "개자식" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "새끼" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "븅딱" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "븅신" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "야발" in message.content:
        await message.delete()
        ch = client.get_channel(863672689612161044)
        await ch.send (f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)