import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import asyncio
import time
import random
import selenium

facts = ['I gave Donald the pass','We came into a broken world. And were the cleanup crew.','If you have the opportunity to play this game of life you need to appreciate every moment. a lot of people don’t appreciate the moment until it’s passed.','We all self-conscious. I’m just the first to admit it.','If I was just a fan of music, I would think that I was the number one artist in the world.','Love your haters, they’re your biggest fans.','I love it','Every man loves men. Facts.','The prettiest people do the ugliest things.']
token = "NTMzMjM2NDAxMzExOTczMzc2.Dx5p9w.c6vyN5dsgLlyktPg19eImJUtw8Q"
Client = discord.Client()
client = commands.Bot(command_prefix = "kanye, ")

@client.event
async def on_ready():
    print("Im ready")
    while True:
        await client.change_presence(game=Game(name='for ur commands ( ͠° ͟ʖ ͠°)', type = 3))


@client.event
async def on_message(message):
    if message.content == "kanye, ping":
        randomd = random.randint(0,10)
        if randomd == 10:
            await client.send_message(message.channel, "fuck off")
        else:
            await client.send_message(message.channel, "pong")
    if message.content.startswith("kanye, fees "):
        userAmountPounds = message.content[11:]
        userAmountPennies = int(userAmountPounds)*100
        print(userAmountPennies)
        paypalOutput = round((((userAmountPennies * 0.969) - 20) / 100) ,2)
        print('Paypal:',paypalOutput)
        ebayOutput = round(((((userAmountPennies * 0.9) * 0.969) - 20) / 100) ,2)
        print('Ebay:',ebayOutput)
        depopOutput = round(((((userAmountPennies * 0.9) * 0.969) - 20) / 100) ,2)
        print('Depop:',depopOutput)
        bumpOutput = round(((((userAmountPennies * 0.94) * 0.969) - 20) / 100) ,2)
        print('Bump:',bumpOutput)
        stockx1Output = round(((userAmountPennies * 0.875) / 100) ,2)
        print('StockX Lvl1:',stockx1Output)
        stockx2Output = round(((userAmountPennies * 0.88) / 100) ,2)
        print('StockX Lvl2:',stockx2Output)
        stockx3Output = round(((userAmountPennies * 0.885) / 100) ,2)
        print('StockX Lvl3:',stockx3Output)
        stockx4Output = round(((userAmountPennies * 0.89) / 100) ,2)
        print('StockX Lvl4:',stockx4Output)
        titleforEmbed = ('Fees for £',userAmountPounds)
        embed = discord.Embed(title=f'Fees Calculated for £{userAmountPounds}', color=0x2fe14e)
        embed.add_field(name='Paypal', value=f'£{paypalOutput}', inline=False)
        embed.add_field(name='Bump', value=f'£{bumpOutput}', inline=False)
        embed.add_field(name='Depop', value=f'£{depopOutput}', inline=False)
        embed.add_field(name='Ebay', value=f'£{ebayOutput}', inline=False)
        embed.add_field(name='StockX Seller Level 1', value=f'£{stockx1Output}', inline=False)
        embed.add_field(name='StockX Seller Level 2', value=f'£{stockx2Output}', inline=False )
        embed.add_field(name='StockX Seller Level 3', value=f'£{stockx3Output}', inline=False)
        embed.add_field(name='StockX Seller Level 4', value=f'£{stockx4Output}', inline=False)
        embed.set_author(name="Kanye's Fee Calculator", icon_url="https://cdn.discordapp.com/attachments/533238248781250563/534686598172770304/Energy-Appraiser-Certification-Registration-Fees-Icon.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/533238248781250563/534687466540630016/image0.jpg")
        embed.set_footer(text="Kanye Bot made by Plug#5464")
        await client.send_message(message.channel,embed=embed)
    if message.content.startswith("kanye, fact"):
        embed = discord.Embed(color=0x2fe14e)
        embed.add_field(name=facts[random.randint(0,(len(facts)-1))], value='- Kanye West', inline=False)
        embed.set_footer(text="Kanye Bot made by Plug#5464")
        await client.send_message(message.channel,embed=embed)
        






client.run(token)
