from discord.ext import commands
import tools
import dbmanagement
import settings


class sfw():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fang(self):
        """For girls with cute little fangs"""
        res = tools.fetch('cutelittlefangs')
        await self.client.say(res.url)

    @commands.command()
    async def tsundere(self):
        """B-Baka!"""
        res = tools.fetch('Tsunderes')
        await self.client.say(res.url)

    @commands.command()
    async def ponytail(self):
        """Some ponytailed girls"""
        res = tools.fetch('animeponytails')
        await self.client.say(res.url)

    @commands.command()
    async def pout(self):
        """:<"""
        res = tools.fetch('pouts')
        await self.client.say(res.url)

    @commands.command(aliases=["kawaii"])
    async def aww(self):
        """Cute anime girls !"""
        res = await dbmanagement.getRandomPostFromDB(settings.db, 'awwnime')
        await self.client.say(res)

def setup(client):
    client.add_cog(sfw(client))