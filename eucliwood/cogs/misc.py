import discord 
import random

from discord.ext import commands

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def on_member_join(self, member):
         # send an intro message upon joining server
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

    @commands.command()
    async def ping(self, ctx):
        """ Ping! """
        to_send = 'Pong!'
        await ctx.channel.send(to_send)

    # @commands.command()
    # async def pingr(sender):
    #     p = '\N{REGIONAL INDICATOR P)'
    #     o = '\N{REGIONAL INDICATOR O)'
    #     n = '\N{REGIONAL INDICATOR N)'
    #     g = '\N{REGIONAL INDICATOR G)'
    #     react(sender, p, o, n, g)

    @commands.command(aliases=['avi', ])
    async def avatar(self, ctx, member : discord.Member = None):
        """ Grabs the tagged user's avatar. If no one is tagged, grabs sender's avatar. """
        await ctx.send(member.avatar_url if member != None else ctx.author.avatar_url)
    
    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

def setup(bot):
    bot.add_cog(Welcome(bot))
