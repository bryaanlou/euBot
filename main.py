import discord 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------')

client = MyClient()
token = open("token", "r")
client.run(token.readline())    