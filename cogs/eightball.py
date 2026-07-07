import discord
from discord.ext import commands
import random

class Eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Eightball.py is ready!")

    
# MAIN FUNCTION
    @commands.command(aliases=["8ball", "eight ball", "8 ball"])
    async def eightball(self, ctx, *, question=None):
        if question:
            with open("Magic/responses.txt", "r") as f:
                random_responses = f.readlines()
                response = random.choice(random_responses)
            await ctx.send(response)
        else:
            await ctx.send("You did not ask me a question")

async def setup(bot):
    await bot.add_cog(Eightball(bot))