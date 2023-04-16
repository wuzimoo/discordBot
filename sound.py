import discord
import youtube_dl

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.content.startswith('!play'):
        channel = message.author.voice.channel
        voice_client = await channel.connect()
        url = message.content[6:]
        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(URL))
        await message.channel.send(f'Now playing: {info["title"]}')

    if message.content.startswith('!leave'):
        await message.guild.voice_client.disconnect()


