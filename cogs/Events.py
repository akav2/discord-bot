import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Events.py is ready!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        log_channel = discord.utils.get(message.guild.channels, name="﹒logs")

        event_embed = discord.Embed(title="Message Logged", description="Message's contents and origins.", color=discord.Colour.dark_green())

        event_embed.add_field(name="Author:", value=message.author.mention, inline=False)
        event_embed.add_field(name="Channel:", value=message.channel.mention, inline=False)
        event_embed.add_field(name="Message:", value=message.content, inline=False)

        await log_channel.send(embed=event_embed)


async def setup(bot):
    await bot.add_cog(Events(bot))