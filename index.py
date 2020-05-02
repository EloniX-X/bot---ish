import discord
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='$')
status = cycle(['becoming a cheese cultist', 'destroying humans', 'DAMMIT JONNY SHUT THE FONT DOR'])


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    change_status.start()
 #   await bot.change_presence(status=discord.Status.idle, activity=discord.Game('eating bananas'))


@bot.command()
async def add(ctx, a: float, b: float):
    await ctx.send(a+b)

@tasks.loop(seconds=3)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def multiply(ctx, a: float, b: float):
    await ctx.send(a*b)

@bot.command()
async def divide(ctx, a: float, b: float):
    await ctx.send(a/b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cutie(ctx):
    await ctx.send(":hot_face: you are all sexy!")

@bot.command()
async def life(ctx):
    await ctx.send("we are all just sex fruit")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def annoyed(ctx):
    await ctx.send("https://media.giphy.com/media/UWKGHQa8ze32U/giphy.gif")

@bot.command()
async def dog(ctx):
    await ctx.send("https://media.giphy.com/media/RQSuZfuylVNAY/giphy.gif")

@bot.command()
async def woah(ctx):
    await ctx.send("https://media.giphy.com/media/26CaLKiimsm3ibpE4/giphy.gif")

@bot.command()
async def sad(ctx):
    await ctx.send("https://media.giphy.com/media/qQdL532ZANbjy/giphy.gif")

@bot.command()
async def why(ctx):
    await ctx.send("https://media.giphy.com/media/gd09Y2Ptu7gsiPVUrv/giphy.gif")

@bot.command()
async def subtract(ctx, a: float, b: float):
    await ctx.send(a-b)

@bot.command()
async def volume(ctx, a: float, b: float, c: float, d: float):
    await ctx.send(a*b*c*d)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Eloni exept bot", description="Eloni is a god and he made this bot thes commands:", color=0xeee657)

    embed.add_field(name="$subtract # - #", value="Gives subtraction of **X** and **Y**", inline=False)
    embed.add_field(name="$add # + #", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply # * #", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$gifs", value="a gif library", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$divide", value="devides # by #", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def gifs(ctx):
    embed = discord.Embed(title="gif library", description="Eloni some funny gifs to lighten up your day:",
                          color=0xeee657)

    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$dog", value="gives a cute dog gif to lighten up your mood", inline=False)
    embed.add_field(name="$woah", value="gives a cute chicken gif to lighten up your mood", inline=False)
    embed.add_field(name="$annoyed", value="gives a annoyed gif to lighten up your mood", inline=False)
    embed.add_field(name="$sad", value="gives a cute dog gif to lighten up your mood", inline=False)
    embed.add_field(name="$why", value="gives a cute dog gif to lighten up your mood", inline=False)
    embed.add_field(name="$dog", value="gives a cute dog gif to lighten up your mood", inline=False)

    await ctx.send(embed=embed)






bot.run(':P')
