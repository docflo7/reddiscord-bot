from discord.ext import commands
from tools import tools

class sfw():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fang(self):
        """For girls with cute little fangs"""
        res = tools.fetch(self, 'cutelittlefangs')
        await self.client.say(res.url)

    @commands.command()
    async def tsundere(self):
        """B-Baka!"""
        res = tools.fetch(self, 'Tsunderes')
        await self.client.say(res.url)

    @commands.command()
    async def ponytail(self):
        """Some ponytailed girls"""
        res = tools.fetch(self, 'animeponytails')
        await self.client.say(res.url)

    @commands.command()
    async def pout(self):
        """:<"""
        res = tools.fetch(self, 'pouts')
        await self.client.say(res.url)

    @commands.command(aliases=["kawaii"])
    async def aww(self):
        """Cute anime girls !"""
        res = tools.fetchV2(self, 'awwnime')
        await self.client.say(res.url)

def setup(client):
    client.add_cog(sfw(client))