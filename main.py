import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def rename(ctx, a:str): # Создаём функцию и передаём аргумент ctx.
    user = ctx.message.mention
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}! {user.mention}') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command(name="id")
async def id_(ctx, user: discord.User):
    await ctx.send(user.id)

async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

@bot.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена