import discord
from discord.ext.commands import Bot


TOKEN = 'NTI2Mzk0NzUxMjc3MjAzNDg2.XkkFgA.xqV-hNpg-ZBh93soSe1VfG6KPAA'

"""client = discord.Client()"""
my_bot = Bot(command_prefix="!")

@my_bot.remove_command("help")
@my_bot.command(name='help',
                description='Pomoc i podstawowe informacje o serwerze',
                aliases=['h','info'])
async def help(ctx):
    helpArray='Witamy {0.author.mention}'.format(ctx)+' w dziale pomocy.\nWpisz !commands w celu sprawdzenia komend\nWpisz !reg w celu sprawdzenia regulaminu\nWpisz !als w celu sprawdzenia skrótów\nMiłych rozmów ;)'
    #if ctx.message.author.server_permissions.ADMINISTRATOR:
    #    await ctx.message.channel.send('POMOC ADMINA\n'+helpArray+'\nWpisz !clear <liczba>, by wyczyścić liczbę wiadomości (domyślnie:10)')
    #else:
    #    await ctx.message.channel.send(helpArray)
    await ctx.message.channel.send(helpArray)


@my_bot.command(name='commands',
                description='Lista komend',
                aliases=['cmd'])
async def commands(ctx):
    commandsArray='!help [!h] - Podstawowe informacje\n!commands [!cmd] - Komendy\n!skroty [!als] - Skrotowe komendy'
    await ctx.message.channel.send(commandsArray)


@my_bot.command(name='aliases',
               description='Lista aliasow komend',
               aliases=['als','skroty'],
                color='red')
async def aliases(ctx):
    aliasesArray='!help <=> !help, !h, !info\n\!commands <=> !commands, !cmd\n\!register <=> !register, !reg\n!aliases <=> !aliases, !als, !skroty\n'
    await ctx.message.channel.send(aliasesArray)

@my_bot.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)



@my_bot.event
async def on_ready():
    print('Logged in as')
    print(my_bot.user.name)
    print(my_bot.user.id)
    print('------')

my_bot.run(TOKEN)