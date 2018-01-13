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

        Will return a random post matching the query in the given subreddit
        By adding sfw or nsfw at the beginning of your query, you can filter for safe/not safe results.
        (Will default to nsfw if not provided)
        """
        safe = False
        if query.startswith("sfw "):
            safe = True
            query = query[4:]
        elif query.startswith("nsfw "):
            query = query[5:]
        res = await tools.searchReddit(sub, query, safe)
        if res is None:
            await self.client.say("No matching post found.\nYou may try again, it could be a timeout.")
        else:
            await self.client.say(res.url)


def setup(client):
    client.add_cog(Utilities(client))
