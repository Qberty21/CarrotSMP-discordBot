import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])

@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author #Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Kek, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
