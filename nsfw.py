import settings
import asyncio
import discord
from discord.ext import commands
from tools import tools

class nsfw():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def zr(self):
        """Zettai Ryouiki"""
        res = tools.fetch(self, 'ZettaiRyouiki')
        await self.client.say(res.url)

    @commands.command()
    async def thh(self):
        """Girls in tigh-highs soing... things"""
        res = tools.fetch(self, 'thighhighhentai')
        await self.client.say(res.url)

    @commands.command()
    async def flat(self):
        """Flat is justice !"""
        res = tools.fetchV2(self, 'chiisaihentai')
        await self.client.say(res.url)

    @commands.command()
    async def legwear(self):
        """Socks, thigh-highs, tights and other things that hug legs!"""
        res = tools.fetch(self, 'animelegwear')
        await self.client.say(res.url)

    @commands.command()
    async def pantsu(self):
        """Slightly NSFW anime girls"""
        res = tools.fetch(self, 'pantsu')
        await self.client.say(res.url)

    @commands.command()
    async def sukebei(self):
        """More NSFW anime girls"""
        res = tools.fetch(self, 'Sukebei')
        await self.client.say(res.url)

    @commands.command()
    async def ecchi(self):
        """NSFW anime girls"""
        res = tools.fetch(self, 'ecchi')
        await self.client.say(res.url)

    @commands.command()
    async def hentai(self):
        """Really ??"""
        res = tools.fetch(self, 'hentai')
        await self.client.say(res.url)

    @commands.command(aliases=['neko'])
    async def nekogirl(self):
        """Because we love nekos"""
        res = tools.fetch(self, 'nekogirls')
        await self.client.say(res.url)

    @commands.command()
    async def nekomimi(self):
        """Because we never have enough nekos !"""
        res = tools.fetch(self, 'Nekomimi')
        await self.client.say(res.url)

    @commands.command()
    async def twintail(self):
        """Two is better than one !"""
        res = tools.fetch(self, 'twintails')
        await self.client.say(res.url)

def setup(client):
    client.add_cog(nsfw(client))