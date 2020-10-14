import discord
import requests
import json
import bs4 as bs
import sports as sn
import asyncio
import time
import covid as c19

messages = 0
joined = 0
Server_Token = 'NjM5ODM4MzEyOTAyOTUwOTI1.XbxF3Q.VOxqQYT8QtfWrVjUr2j8yrhx9Y0'

client = discord.Client(intents=discord.Intents(messages=True, guilds=True))

async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(30)
        except Exception as e:
            print(e)
            await asyncio.sleep(30)

@client.event
async def on_ready():
    print('We have logged on as {0.user}'.format(client))



@client.event
async def on_disconnect():
    print('{0.user} has successfully disconnected from server'.format(client))



@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1

    bad_words = ["Fuck", "Bastard", "insert_word"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
            await message.channel.send("We do not tolerate bad language in this server")


    if message.author == client.user:
        return


    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


#This is the help section
    if message.content == "!help":
        embed = discord.Embed(title="You useless prick heres the commands", description="retard guide")
        embed.add_field(name="!hello", value="Obviously says hello back he's not a dick")
        embed.add_field(name="!help", value="brings up this shit")
        embed.add_field(name="!Football", value="Latest Sky Sports football news with links!!!")
        await message.channel.send(content=None, embed=embed)


#gets latest football news from sky sports webpage
    if message.content.startswith('!Football'):
        embed = discord.Embed(title="Football news", description="Football news from sky sports")
        embed.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJyfZXEICfqq4_K3WUSJENVh8IlQ7RNS9LMFisoy8A=s900-c-k-c0xffffffff-no-rj-mo')
        headlines, links = sn.get_news()
        i = 0
        inl = False
        for headline in headlines:
            if i % 2 == 0:
                inl = False
            else:
                inl = True

            embed.add_field(name ="Headline {}.".format(i + 1), value="[{}]({})".format(headline, links[i]), inline=inl)
            i += 1
#embed.add_field(name="Field title", value="Your text here: [link](http://example.com)")
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("!covid graph"):
        embed = discord.Embed(title="Covid Graph", description="A graphical representation of live time covid-19 cases in ireland")
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1200px-SARS-CoV-2_without_background.png')
        await message.channel.send(content=None, embed=embed)
        c19.make_plot('Ireland')
        file = discord.File("covid_graph.png", filename="covid_graph.png")
        await message.channel.send('covid_graph.png', file=file)


        
client.loop.create_task(update_stats())
client.run(Server_Token)
