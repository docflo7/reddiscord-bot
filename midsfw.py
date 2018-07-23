from discord.ext import commands
import tools
import dbmanagement
import settings


class MIXED_SFW_AND_NSFW():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fang(self):
        """r/cutelittlefangs

        For girls with cute little fangs"""
        res = tools.fetch('cutelittlefangs')
        await self.client.say(res.url)

    @commands.command()
    async def bigfang(self):
        """r/massivefangs

        For people appreciating the variety of fangs"""
        res = tools.fetch('massivefangs')
        await self.client.say(res.url)

    @commands.command()
    async def tying(self):
        """r/tyingherhairup

        Girls tying their hair"""
        res = tools.fetch('tyingherhairup')
        await self.client.say(res.url)

    @commands.command()
    async def imouto(self):
        """r/imouto

        I guess there are some siscons here"""
        res = tools.fetch('imouto')
        await self.client.say(res.url)

    @commands.command()
    async def zr(self):
        """r/ZettaiRyouiki

        legwear and skirts"""
        res = tools.fetch('ZettaiRyouiki')
        await self.client.say(res.url)

    @commands.command()
    async def legwear(self):
        """r/animelegwear

        Socks, thigh-highs, tights and other things that hug legs!"""
        res = tools.fetch( 'animelegwear')
        await self.client.say(res.url)

    @commands.command(aliases=["twintails"])
    async def twintail(self):
        """r/twintails

        Two is better than one !"""
        res = tools.fetch('twintails')
        await self.client.say(res.url)


def setup(client):
    client.add_cog(MIXED_SFW_AND_NSFW(client))
