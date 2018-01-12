from discord.ext import commands
import praw
import random
import dbmanagement
import auth


def init():
    global reddit
    global client
    global startup_extensions
    global img_extensions
    global db
    global wavingStatus
    global appinfo

    client = commands.Bot(description="reddit image picker bot - by docflo7", command_prefix=auth.discord_command_prefix, pm_help=False)
    reddit = praw.Reddit(client_id=auth.reddit_client, client_secret=auth.reddit_secret, user_agent='discord_bot')

    # this specifies what extensions to load when the bot starts up
    startup_extensions = ["nsfw", "sfw", "admin"]
    # image extensions to filter
    img_extensions = [".jpg", ".png", ".jpeg", ".bpm", ".gif"]
    # this specifies what subreddits need to be cached
    # some subreddits can't be browsed by the praw random function and need this
    cached_subreddits = ["awwnime", "chiisaihentai"]
    # get the db connection
    db = dbmanagement.connectDB(client, reddit, cached_subreddits)
    # seed the PRNG
    random.seed()

    # global variables across modules
    reactionsStatus = True
    appinfo = None
