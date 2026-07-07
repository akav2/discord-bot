import discord
from discord.ext import commands
import random
import os
import asyncio
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN= str = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Vita is connected to discord!") 



# user info command

@bot.command(aliases=["ui", "USERINFO"])
async def userinfo(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member

    info_embed = discord.Embed(title=f"{member.name}'s User Information", description="Infortmation relating to this user.", color=member.color)
    info_embed.set_thumbnail(url=member.avatar)
    info_embed.add_field(name="Username:", value=member.name, inline=False)
    info_embed.add_field(name="Nickname:", value=member.display_name, inline=False)
    info_embed.add_field(name="UserID:", value=member.id, inline=False)
    info_embed.add_field(name="Top role:", value=member.top_role, inline=False)
    info_embed.add_field(name="Join date:", value=member.joined_at, inline=False)
    info_embed.add_field(name="Account creation:", value=member.created_at.__format__("%A, %d. %B %Y"), inline=False)

    await ctx.send(embed=info_embed)



async def load():
    for filename in os.listdir("./cogs"): 
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)   

asyncio.run(main())   