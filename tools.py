import settings
import random


def init():
    global reddit
    global img_extensions
    reddit = settings.reddit
    img_extensions = settings.img_extensions


# This is the function browsing a given subreddit
def fetch(sub, bypass=False):
    subr = reddit.subreddit(sub)
    lastChannel = settings.lastChannel
    i = 0
    while True:
        subm = subr.random()
        if check_img_link(subm.url):
            i += 1
            #print(subm.url)
            if bypass:
                return subm
            if (lastChannel != "nsfw" and subm.over_18) or (lastChannel == "nsfw" and not subm.over_18):
                if i >= 50:
                    # TODO : change this because it's ugly
                    subm.url = "Sorry, but that didn't work :frowning:"
                    return subm
                pass
            else:
                return subm


# This is another version of the function browsing a given subreddit
# This one bypasses the invalid url error from certain subreddits
# This method is deprecated because of how unefficient it was.
# You should use the cached version : getRandomPostFromDB, located in dbmanagement.py
def fetchV2(sub):
    subr = reddit.subreddit(sub)
    posts = [post for post in subr.new(limit=500)]
    while True:
        random_post_number = random.randint(0, 500)
        random_post = posts[random_post_number]
        if check_img_link(random_post.url):
            # print(random_post.url)
            return random_post


async def searchReddit(sub, query, safe):
    subr = reddit.subreddit(sub)
    posts = [post for post in subr.search(query)]
    limit = 0
    if len(posts) == 0:
        return None
    while limit <= 200:
        random_post_number = random.randint(0, len(posts) - 1)
        random_post = posts[random_post_number]
        if check_img_link(random_post.url):
            if safe and random_post.over_18:
                pass
            else:
                return random_post
        limit += 1
    return None


def is_owner(ctx):
    owner = settings.appinfo.owner
    return ctx.message.author.id == owner.id


def is_lord(ctx):
    return ctx.message.author.id == ctx.message.server.owner.id


def is_owner_or_lord(ctx):
    owner = settings.appinfo.owner
    return (ctx.message.author.id == owner.id) or (ctx.message.author.id == ctx.message.server.owner.id)


def check_img_link(link):
    for extension in img_extensions:
        if link.endswith(extension):
            return True
    if link.startswith("https://imgur.com/"):
        return True
    elif link.startswith("http://imgur.com/"):
        return True
    else:
        return False
