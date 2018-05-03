from discord.ext import commands
import tools
import dbmanagement
import settings


class SFW_ONLY():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tsundere(self):
        """r/Tsunderes

        B-Baka!"""
        res = tools.fetch('Tsunderes')
        await self.client.say(res.url)

    @commands.command()
    async def ponytail(self):
        """r/animeponytails

        Some ponytailed girls"""
        res = tools.fetch('animeponytails')
        await self.client.say(res.url)

    @commands.command()
    async def pout(self):
        """r/pouts

        :<"""
        res = tools.fetch('pouts')
        await self.client.say(res.url)

    # unactive due to reddit random bug (cf issue 885 of PRAW)
    # @commands.command()
    async def kanmusu(self):
        """r/KanMusu

        Cute shipgirls
        (Shigure best girl btw)"""
        res = tools.fetch('KanMusu')
        await self.client.say(res.url)

    @commands.command(aliases=["kawaii"])
    async def aww(self):
        """r/awwnime

        Cute anime girls !"""
        res = await dbmanagement.getRandomPostFromDB(settings.db, 'awwnime')
        await self.client.say(res)
    
    @commands.command(aliases=["short"])
    async def shorthair(self):
        """r/shorthairedwaifus

        Anime girls lacking hair length"""
        res = tools.fetch('shorthairedwaifus')
        await self.client.say(res.url)

    @commands.command(aliases=["long"])
    async def longhhair(self):
        """r/longhairedwaifus

        Adorable girls with flowing long hair"""
        res = tools.fetch('longhairedwaifus')
        await self.client.say(res.url)


def setup(client):
    client.add_cog(SFW_ONLY(client))
