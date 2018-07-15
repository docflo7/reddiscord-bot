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
    global reactionsStatus
    global appinfo
    global lastChannel
    global cooldown
    global NSFW_chan

    client = commands.Bot(description="reddit image picker bot - by docflo7", command_prefix=auth.discord_command_prefix, pm_help=False)
    reddit = praw.Reddit(client_id=auth.reddit_client, client_secret=auth.reddit_secret, user_agent='discord_bot')

    # this specifies what extensions to load when the bot starts up
    startup_extensions = ["nsfw", "sfw", "midsfw", "admin", "utilities", "osu"]

    # image extensions to filter
    img_extensions = [".jpg", ".png", ".jpeg", ".bmp", ".gif"]

    # this specifies what subreddits need to be cached
    # some subreddits can't be browsed by the praw random function and need this
    cached_subreddits = ["awwnime", "chiisaihentai"]  #, "doujinshi"]

    # get the db connection
    db = dbmanagement.connectDB(client, reddit, cached_subreddits)

    # seed the PRNG
    random.seed()
    
    # global variables across modules
    reactionsStatus = True
    appinfo = None
    lastChannel = ""
    cooldown = 0
    NSFW_chan = ['247923826237767690', '391493353688137730', '402220753350688768']

