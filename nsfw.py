from discord.ext import commands
import tools
import dbmanagement
import settings


class NSFW_ONLY():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def thh(self):
        """r/tighhighhentai

        Girls in tigh-highs doing... things"""
        res = tools.fetch('thighhighhentai')
        await self.client.say(res.url)

    @commands.command()
    async def flat(self):
        """r/chiisaihentai

        Flat is justice !"""
        if settings.lastChannel in settings.NSFW_chan:
          res = await dbmanagement.getRandomPostFromDB(settings.db, 'chiisaihentai')
          await self.client.say(res)
        else:
          await self.client.say("W-W-What ? I can't post things like that in a safe channel, it would be embarrassing !")

    @commands.command()
    async def oppai(self):
        """r/dekaihentai

        For the titty lovers"""
        res = tools.fetch('dekaihentai')
        await self.client.say(res.url)

    @commands.command()
    async def pantsu(self):
        """r/pantsu

        Slightly NSFW anime girls"""
        res = tools.fetch('pantsu')
        await self.client.say(res.url)

    @commands.command()
    async def sukebei(self):
        """r/Sukebei

        More NSFW anime girls"""
        res = tools.fetch('Sukebei')
        await self.client.say(res.url)

    @commands.command()
    async def ecchi(self):
        """r/ecchi

        NSFW anime girls"""
        res = tools.fetch('ecchi')
        await self.client.say(res.url)

    # @commands.command()
    async def doujinshi(self):
        """r/doujinshi

        (ero-)mangas drawings"""
        if settings.lastChannel in settings.NSFW_chan:
          res = await dbmanagement.getRandomPostFromDB(settings.db, 'doujinshi')
          await self.client.say(res)
        else:
          await self.client.say("W-W-What ? I can't post things like that in a safe channel, it would be embarrassing !")

    @commands.command()
    async def hentai(self):
        """r/hentai

        Really ??"""
        res = tools.fetch('hentai')
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
        res = tools.fetch('nekogirls')
        await self.client.say(res.url)

    @commands.command()
    async def nekomimi(self):
        """r/Nekomimi

        Because we never have enough nekos !"""
        res = tools.fetch('Nekomimi')
        await self.client.say(res.url)

    # unactive due to reddit random bug (cf issue 885 of PRAW)
    # @commands.command(aliases=["kanmusunight"])
    async def kanmusunights(self):
        """r/KanMusuNights

        Shipgirls having good time
        (Shigure best girl btw)"""
        res = tools.fetch('KanMusuNights')
        await self.client.say(res.url)


def setup(client):
    client.add_cog(NSFW_ONLY(client))
