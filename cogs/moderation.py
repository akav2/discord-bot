import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is ready!")

# CLEAR COMMAND
    @commands.command(aliases=["c"])
    @commands.cooldown(2, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        max_limit = 250
        if count > max_limit:
            await ctx.send("You can not purge that many messages.")
            return
        await ctx.message.delete()
        await ctx.channel.purge(limit=count)


# COOLDOWN 
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            time_left = round(error.retry_after, 1)
            await ctx.send(f"Boy Slow down.", delete_after=3)

# KICK COMMAND

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, memeber: discord.Member, *, modreason):
    await ctx.guild.kick(memeber)

    conf_embed=discord.Embed(title="Success!", color=discord.Color.black())
    conf_embed.add_field(name="Kicked:", value=f"{memeber.mention} has been kicked", inline=False)
    conf_embed.add_field(name="Reason:", value=modreason, inline=False)

    await ctx.send(embed=conf_embed)

# BAN COMMAND

@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(self, ctx, memeber: discord.Member, *, modreason):
    await ctx.guild.ban(memeber)

    conf_embed=discord.Embed(title="Success!", color=discord.Color.black())
    conf_embed.add_field(name="Banned:", value=f"{memeber.mention} has been banned", inline=False)
    conf_embed.add_field(name="Reason:", value=modreason, inline=False)

    await ctx.send(embed=conf_embed)


# UNBAN COMMAND

@commands.command(name="unban")
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, userId):
    user = discord.Object(id=int(userId))
    await ctx.guild.unban(user)

    conf_embed=discord.Embed(title="Success!", color=discord.Color.black())
    conf_embed.add_field(name="Unbanned:", value=f"{userId} has been unbanned.", inline=False)

    await ctx.send(embed=conf_embed)




async def setup(bot):
    await bot.add_cog(Moderation(bot))

    