import discord
from discord.ext import commands
import asyncio
import sqlite3 as sql
from config import settings, ban_word
from db import dataBase


intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

# async def send_msg(channel, text):
#     channel = bot.get_channel(channel)
#     await channel.send(text)


class Buttons(discord.ui.View):  # класс описывает набор кнопок
    def __init__(self, *, timeout=180):  # конструктор класса
        super().__init__(timeout=timeout)
    # этому методу будет сопоставлена кнопка. По клику метод будет вызван.
    @discord.ui.button(label="Button",style=discord.ButtonStyle.gray)
    async def gray_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        # ищи сведения об объекте discord.Interaction, чтобы понять, что ещё можно сделать в обработчике кнопки.
        await interaction.response.edit_message(content=f"This is an edited button response!")
        # альтернативно, тут ты можешь вызывать требуемые тебе методы и вообще делать что нужно

@bot.event
async def on_message(ctx : discord.message.Message):
    onn_status = dataBase.select_onn(ctx.guild.id)
    if onn_status['text'] == "True":
        for i in ban_word: # Проверка всех сообщений на бан ворды
            if i in ctx.content:
                await ctx.reply("Сообщение удалено")
                await ctx.delete()
                break
    if ctx.content.startswith(f'{settings["prefix"]}settings'):
        dataBase.of_or_on_protect(ctx.guild.id)
        await ctx.channel.send("Настройки изменены")
    if ctx.content.startswith(f'{settings["prefix"]}button'):
        await ctx.channel.send(
            "This message has buttons!",  # текст сообщения как обычно
            view=Buttons()  # создаём экземпляр класса Buttons и прикрепляем его
        )
    if ctx.content.startswith(f'{settings["prefix"]}button'):
        await ctx.channel.send(
            "This message has buttons!",  # текст сообщения как обычно
            view=Buttons()  # создаём экземпляр класса Buttons и прикрепляем его
        )


@bot.event
async def on_guild_join(guild : discord.guild.Guild):
    dataBase.insert_guild(guild_id=guild.id, onn="True")
    ctx =  guild.get_channel(guild.channels[0].id)
    await ctx.text_channels[0].send("Всем привет, я готов к работе")
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
