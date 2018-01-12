from discord.ext import commands
import tools
import dbmanagement
import settings


class NSFW():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def zr(self):
        """Zettai Ryouiki"""
        res = tools.fetch( 'ZettaiRyouiki')
        await self.client.say(res.url)

    @commands.command()
    async def thh(self):
        """Girls in tigh-highs soing... things"""
        res = tools.fetch( 'thighhighhentai')
        await self.client.say(res.url)

    @commands.command()
    async def flat(self):
        """Flat is justice !"""
        res = await dbmanagement.getRandomPostFromDB(settings.db, 'chiisaihentai')
        await self.client.say(res)

    @commands.command()
    async def legwear(self):
        """Socks, thigh-highs, tights and other things that hug legs!"""
        res = tools.fetch( 'animelegwear')
        await self.client.say(res.url)

    @commands.command()
    async def pantsu(self):
        """Slightly NSFW anime girls"""
        res = tools.fetch( 'pantsu')
        await self.client.say(res.url)

    @commands.command()
    async def sukebei(self):
        """More NSFW anime girls"""
        res = tools.fetch( 'Sukebei')
        await self.client.say(res.url)

    @commands.command()
    async def ecchi(self):
        """NSFW anime girls"""
        res = tools.fetch( 'ecchi')
        await self.client.say(res.url)

    @commands.command()
    async def hentai(self):
        """Really ??"""
        res = tools.fetch( 'hentai')
        await self.client.say(res.url)

    @commands.command(aliases=['neko'])
    async def nekogirl(self):
        """Because we love nekos"""
        res = tools.fetch( 'nekogirls')
        await self.client.say(res.url)

    @commands.command()
    async def nekomimi(self):
        """Because we never have enough nekos !"""
        res = tools.fetch( 'Nekomimi')
        await self.client.say(res.url)

    @commands.command()
    async def twintail(self):
        """Two is better than one !"""
        res = tools.fetch( 'twintails')
        await self.client.say(res.url)


def setup(client):
    client.add_cog(NSFW(client))
