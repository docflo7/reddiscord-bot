from discord.ext import commands
import tools
import dbmanagement
import settings


class NSFW():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def zr(self):
        """r/ZettaiRyouiki

        legwear and skirts"""
        res = tools.fetch( 'ZettaiRyouiki')
        await self.client.say(res.url)

    @commands.command()
    async def thh(self):
        """r/tighhighhentai

        Girls in tigh-highs soing... things"""
        res = tools.fetch( 'thighhighhentai')
        await self.client.say(res.url)

    @commands.command()
    async def flat(self):
        """r/chiisaihentai

        Flat is justice !"""
        res = await dbmanagement.getRandomPostFromDB(settings.db, 'chiisaihentai')
        await self.client.say(res)

    @commands.command()
    async def legwear(self):
        """r/animelegwear

        Socks, thigh-highs, tights and other things that hug legs!"""
        res = tools.fetch( 'animelegwear')
        await self.client.say(res.url)

    @commands.command()
    async def pantsu(self):
        """r/pantsu

        Slightly NSFW anime girls"""
        res = tools.fetch( 'pantsu')
        await self.client.say(res.url)

    @commands.command()
    async def sukebei(self):
        """r/Sukebei

        More NSFW anime girls"""
        res = tools.fetch( 'Sukebei')
        await self.client.say(res.url)

    @commands.command()
    async def ecchi(self):
        """r/ecchi

        NSFW anime girls"""
        res = tools.fetch( 'ecchi')
        await self.client.say(res.url)

    @commands.command()
    async def doujinshi(self):
        """r/doujinshi

        ero-mangas"""
        res = tools.fetch( 'doujinshi')
        await self.client.say(res.url)

    @commands.command()
    async def hentai(self):
        """r/hentai

        Really ??"""
        res = tools.fetch( 'hentai')
        await self.client.say(res.url)

    @commands.command()
    async def yuri(self):
        """r/yuri

        For girls liking girls"""
        res = tools.fetch('yuri')
        await self.client.say(res.url)

    @commands.command(aliases=['neko'])
    async def nekogirl(self):
        """r/nekogirls

        Because we love nekos"""
        res = tools.fetch( 'nekogirls')
        await self.client.say(res.url)

    @commands.command()
    async def nekomimi(self):
        """r/Nekomimi

        Because we never have enough nekos !"""
        res = tools.fetch( 'Nekomimi')
        await self.client.say(res.url)

    @commands.command(aliases=["twintails"])
    async def twintail(self):
        """r/twintails

        Two is better than one !"""
        res = tools.fetch( 'twintails')
        await self.client.say(res.url)


def setup(client):
    client.add_cog(NSFW(client))
