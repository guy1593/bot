import discord
import time
import urllib.request
import re
import asyncio
import random

client = discord.Client()
channels = ["cup"]
shut = ["Bob'nt#8977"]

messages = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(721362101267988480)
    channels = ["cup"]
    strip = '@' + str(message.author).strip("#0123456789")
    valid_users = ['CommanderGuy#0360','ofekmek#3242','NOT_BOB#8977','fatto catto#9913','wtf#0981','flotation#1218','Barvuz#1050',"Bob'nt#8977",'☆SnowCrystalz☆#6555']
    responses = ['K good job','Well done pathetic human','I am proud of you']

    if message.content.find("!help") != -1:
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello",value="Greets the user")
        embed.add_field(name="!finger", value="Sends a third finger emoji")
        embed.add_field(name="!gay",value="Someone is a gay")
        embed.add_field(name='barvuz',value='The youtube search engine')
        await message.channel.send(content=None,embed=embed)

    if True:
        if message.content.find("!hello") != -1:
            await message.channel.send('Hi Bitch')

        if message.content.find("!finger") != -1:
            await message.channel.send(':middle_finger_tone1:')

        if message.content.find("!gay") != -1:
            for v in valid_users:
                if str(message.content[-5:]) in v:
                    await message.channel.send(f'{v} is Gay')
            else:
                await message.channel.send(f'{message.author} you are gay now')

        if message.content.find("cup") != -1:
            await message.channel.send(random.choice(responses))

        if message.content.find('barvuz') != -1:
            await message.channel.send("Barvuz™️ is now setting up please wait...")

            searchcleaner = str(message.content).lstrip('barvuz')
            search = 'https://www.youtube.com/results?search_query=' + searchcleaner.strip(" ")
            search2 = search.replace(' ', '+')
            html = urllib.request.urlopen(search2)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            vilink = "https://www.youtube.com/watch?v=" + video_ids[0]

            await message.channel.send('Loading...')
            await message.channel.send(vilink)

        if message.content.find("kys") != -1:
            await message.channel.send(f'That was very rude {message.author}, instead, take your own advice.')

        if str(message.author) in shut:
            await message.channel.send('SHUT')

        if message.content.find('!airstrike') != -1:
            await message.channel.send('Calling for air support...')

        if message.content.find('!shentai') != -1:
            searchcleaner2 = str(message.content).lstrip('!shentai')
            search3 = 'https://animeidhentai.com/' + searchcleaner2.strip(" ")
            search4 = search3.replace(' ', '-')
            await message.channel.send(search4)

    else:
        print(f'''User: {message.author} tried to do command {message.content} in channel {message.channel}''')


client.run(NzU5NzIxMDg2MDEwMTMwNDYy.X3BnZQ.uE5xzMrRnBDyAxacrmM3-wNTZl0)
