import discord 
import random

from discord.ext import commands

class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
         # send an intro message upon joining server
        if member.guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, member.guild)
            await member.guild.system_channel.send(to_send)

    @commands.command()
    async def ping(self, ctx):
        """ pong """
        await ctx.channel.send('pong')

    @commands.command()
    async def pingr(self, ctx):
        """ 🇵🇴🇳🇬 """
        await ctx.message.add_reaction('🇵')
        await ctx.message.add_reaction('🇴')
        await ctx.message.add_reaction('🇳')
        await ctx.message.add_reaction('🇬')

    @commands.command(aliases=['avi', ])
    async def avatar(self, ctx, member : discord.Member = None):
        """ Grabs the tagged user's avatar."""
        await ctx.send(member.avatar_url if member != None else ctx.author.avatar_url)
    
    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

def setup(bot):
    bot.add_cog(Miscellaneous(bot))
