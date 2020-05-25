import discord 

class MyClient(discord.Client):

        async def on_member_join(self, member):
            # send an intro message upon joining server
            guild = member.guild
            if guild.system_channel is not None:
                to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
                await guild.system_channel.send(to_send)