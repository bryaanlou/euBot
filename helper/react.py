import discord

class MyContext(commands.Context):
    async def react(self, **emojis):
        # helper function
        # reacts to message with a list of emojis
        try: 
            for emoji in emojis:
                await self.message.add_reaction(emoji)
        except discord.HTTPException:
            # Just gonna ignore all errors :) 
            pass

