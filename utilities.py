from discord.ext import commands
import tools
import dbmanagement
import settings


class Utilities():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def search(self, sub, *, query):
        """Search a post in a subreddit

        Will return a random post matching the query in the given subreddit"""
        res = await tools.searchReddit(sub, query)
        await self.client.say(res.url)


def setup(client):
    client.add_cog(Utilities(client))
