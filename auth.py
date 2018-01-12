# This is the auth file for heroku live version
# If you run this on heroku, just edit you env variables
# otherwise, edit the values from the file

import os
from urllib import parse


def init():
    """test"""
    global discord_command_prefix
    global discord_token
    global reddit_client
    global reddit_secret
    global db_name
    global db_host
    global db_port
    global db_user
    global db_pass

    discord_command_prefix = "<"
    discord_token = os.environ["DISCORD_TOKEN"]
    reddit_client = os.environ["REDDIT_CLIENT"]
    reddit_secret = os.environ["REDDIT_SECRET"]

    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])
    db_name = url.path[1:]
    db_host = url.hostname
    db_port = url.port
    db_user = url.username
    db_pass = url.password
