# Import Discord package
import discord
from discord import embeds
from discord.ext import commands
import asyncio

import pandas_datareader

import random
# Client (bot)
client = commands.Bot(command_prefix='$')
CHANNEL_ID = #

####


# When Bot Connects
@client.event
async def on_ready():
    general_channel = client.get_channel(CHANNEL_ID)  
    await general_channel.send('Hello! The Discord Bot is here!')

# When Bot Disconnects 
@client.event
async def on_disconnect():
    general_channel = client.get_channel(CHANNEL_ID)
    await general_channel.send('Discord Bot Signing Out!')


# Bot Function 
@client.event
async def on_message(message):
    if message.content == 'version':
        general_channel = client.get_channel(CHANNEL_ID)

        myEmbed = discord.Embed(title="Current Version:", description="The Discord Bot is in Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="15/05/21", inline=False)
        myEmbed.set_footer(text="This Bot was Designed and Engineered by Zayd3030")
        myEmbed.set_author(name="Discord Bot")

        await general_channel.send(embed=myEmbed)
    
    await client.process_commands(message)

# Bot Status

async def ch_pr():
    await client.wait_until_ready()

    statuses = ["Game1", "Game2", "Game3", "Game4", "Game5", "Game6"]

    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)

client.loop.create_task(ch_pr())

# Remove Help Command

client = commands.Bot(command_prefix= "$")
client.remove_command("help")

# Embed Help Commands

@client.group(invoke_without_command=True) 
async def help(ctx):
    myEmbed = discord.Embed(title = "Help", description = "Use $help <command> for extended information on a command.", color = 0x00ff00)
    myEmbed.add_field(name = "Moderation", value = "Kick, Ban, Warn")
    myEmbed.add_field(name = "Games", value = "Giveaway")

    await ctx.send(embed = myEmbed)

#Kick
@help.command()
async def kick(ctx):
    myEmbed = discord.Embed(title = "Kick", description = "Kicks a member from the guild", color = 0x00ff00)
    myEmbed.add_field(name = "**Syntax**", value = "$kick <member> [reason]")

    await ctx.send(embed = myEmbed)

#Ban
@help.command()
async def ban(ctx):
    myEmbed = discord.Embed(title = "Ban", description = "Bans a member from the guild", color = 0x00ff00)
    myEmbed.add_field(name = "**Syntax**", value = "$ban <member> [reason]")

    await ctx.send(embed = myEmbed)

#Warn
@help.command()
async def warn(ctx):
    myEmbed = discord.Embed(title = "Warn", description = "Warns a member from the guild", color = 0x00ff00)
    myEmbed.add_field(name = "**Syntax**", value = "$warn <member> [reason]")

    await ctx.send(embed = myEmbed)


@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title="Current Version:", description="The Discord Bot is in Version 1.0.2", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.2", inline=False)
    myEmbed.add_field(name="Date Released:", value="22/05/21", inline=False)
    myEmbed.set_footer(text="This Bot was Designed and Engineered by Zayd3030")
    myEmbed.set_author(name="Discord Bot")

    await context.message.channel.send(embed=myEmbed)
    
#Sends a private direct message to author of command
@client.command(name='private')
async def private(context):
    await context.message.author.send("Hello in Private!")
    
#stock prices

def get_stock_price(ticker):
    data = web.DataReader(ticker, "yahoo")
    return data['Close'].iloc[-1]


@client.event
async def on_message(message):
    if message.content.startswith("$stockprice"):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            await message.channel.send(f"Stock Price of {ticker} is {price}")

    
# Run client on server
client.run('#')
