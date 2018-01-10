import settings
import random

reddit = settings.reddit
img_extensions = settings.img_extensions


class tools():
    def __init__(self, client):
        self.client = client

    # This is the function browsing a given subreddit
    def fetch(self, sub):
        subr = reddit.subreddit(sub)
        while True:
            subm = subr.random()
            ext = subm.url[-4:]
            if ext in img_extensions:
                print(subm.url)
                return subm

    # This is another version of the function browsing a given subreddit
    # This one bypasses the invalid url error from certain subreddits
    def fetchV2(self, sub):
        subr = reddit.subreddit(sub)
        posts = [post for post in subr.new(limit=500)]
        while True:
            random_post_number = random.randint(0, 500)
            random_post = posts[random_post_number]
            ext = random_post.url[-4:]
            if ext in img_extensions:
                print(random_post.url)
                return random_post

    # A better version of the custom function to geet a random reddit post
    # This version uses a cache
    def fetchV3(self, sub):
        return

    def is_owner(ctx):
        owner = settings.appinfo.owner
        return ctx.message.author.id == owner.id

    def is_lord(ctx):
        return ctx.message.author.id == ctx.message.server.owner.id

    def is_owner_or_lord(ctx):
        owner = settings.appinfo.owner
        return (ctx.message.author.id == owner.id) or (ctx.message.author.id == ctx.message.server.owner.id)


def setup(client):
    client.add_cog(tools(client))
