import asyncio
import discord
import platform
from discord.ext import commands
import settings
import auth
import dbmanagement
import tools

#read values from the settings and auth file
auth.init()
settings.init()
tools.init()


client = settings.client
startup_extensions = settings.startup_extensions
appinfo = settings.appinfo

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('--------')
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+')')
    print('Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Connected to reddit as a read-only instance')
    print('--------')
    await client.change_presence(game=discord.Game(name='reddit'))
    await dbmanagement.checkReminder(settings.db, client)
    global appinfo
    appinfo = await client.application_info()
    settings.appinfo = appinfo


@client.check
def globally_block_dms(ctx):
    return ctx.message.server is not None


@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        # print(message)
        if settings.reactionsStatus:
            if message.content.lower() in ['hello', 'hi', 'hallo']:
                await client.send_message(message.channel, 'Hello ' + str(message.author.name))
            if message.content == 'o/':
                await client.send_message(message.channel, '\o')
            if message.content == 'o7':
                await client.send_message(message.channel, 'Yousoro!')
            if message.content.lower() == 'fuck you':
                await client.send_message(message.channel, ':middle_finger:')
            if message.content.lower() == 'this bot sucks':
                await client.send_message(message.channel, "Yeah, sauce-bot sucks... I'm way better")
            if "Kizuna Ai".lower() in message.content.lower():
                try:
                    await client.add_reaction(message, "❤")
                except:
                    # If you bot doesn't have the "READ MESSAGE HISTORY" permission, adding reactions is impossible
                    print("Can't add reaction. Permission denied.")
                await kizuna(message)
        await client.process_commands(message)


@client.event
async def on_command_error(error, ctx):
    print(type(error))
    ignored = (commands.CommandNotFound, commands.UserInputError)
    # The main part of the error handling use the work from :
    # https://gist.github.com/MysterialPy/7822af90858ef65012ea500bcecf1612

    # This prevents any commands with local handlers being handled here in on_command_error.
    if hasattr(ctx.command, 'on_error'):
        return

    # Allows us to check for original exceptions raised and sent to CommandInvokeError.
    # If nothing is found. We keep the exception passed to on_command_error.
    error = getattr(error, 'original', error)

    # Anything in ignored will return and prevent anything happening.
    if isinstance(error, ignored):
        return
    elif isinstance(error, commands.CheckFailure):
        await client.send_message(ctx.message.channel, "Sorry " + ctx.message.author.mention + ", you don't have the permission for this")
    elif isinstance(error, commands.DisabledCommand):
        await client.send_message(ctx.message.channel, f'```The command {ctx.command} is disabled.```')
        return
    elif isinstance(error, commands.NoPrivateMessage):
        try:
            await client.send_message(ctx.message.channel, f'```The command {ctx.command} can not be used in Private Messages.```')
            return
        except:
            pass
    else:
        print(error)


@client.command(name='reload', hidden=True, pass_context=True)
@commands.check(tools.is_owner)
async def _reload(ctx, *, module : str):
    """Reloads a module."""
    try:
        client.unload_extension(module)
        client.load_extension(module)
    except Exception as e:
        if isinstance(e, ImportError):
            await client.say("I can't do that. Does this module exist ?")
        else:
            await client.say("I can't do that. It seems there's an error in this module and I can't load it.\nIt is probably in an unloaded state now.")
        print('{}: {}'.format(type(e).__name__, e))
    else:
        await client.say('Module reloaded')


@client.command(name='unload', hidden=True, pass_context=True)
@commands.check(tools.is_owner)
async def _unload(ctx, *, module : str):
    """Unloads a module."""
    try:
        client.unload_extension(module)
    except Exception as e:
        await client.say("I can't do that. Does this module exist ? Was it loaded ?")
        print('{}: {}'.format(type(e).__name__, e))
    else:
        await client.say('Module unloaded')


@client.group(pass_context=True)
async def remindme(ctx):
        """A set of command to create reminders"""
        if ctx.invoked_subcommand is None:
            await client.say(f"```A set of commands to create reminders : \n{client.command_prefix}remindme now *task* \n\tto be reminder now to do *task* \n{client.command_prefix}remindme in *time* *task* \n\tto be reminded to do *task* in *time* minutes```")


@remindme.command(pass_context=True, name='now')
async def remindmenow(ctx, *, what):
    """send yourself a reminder now"""
    await client.send_message(ctx.message.author, "Don't forget : " + what)


@remindmenow.error
async def remindmenow_handler(error, ctx):
    """A local Error Handler for remindme."""
    await client.say("```You need to say what you want to be reminded```")


@remindme.command(pass_context=True, name='in')
async def remindmein(ctx, time, *, what):
    """send yourself a reminder in *time* minutes"""
    try:
        num = int(time)
        await dbmanagement.addReminder(settings.db, ctx.message.author.id, num, what)
        await client.say("I'll send you a PM later !")
    except ValueError:
        await client.say("...")
        return False


@remindmein.error
async def remindmein_handler(error, ctx):
    """A local Error Handler for remindmein."""
    await client.say("```You need to say in how long I have to remind you, and what```")


@client.command(hidden=True)
async def lemons():
    await client.say(":lemon:")


@client.command(hidden=True)
async def points():
    await client.say("!points")


@client.command(pass_context=True)
async def kawaiidesu(ctx):
    """React to kawaii things"""
    await client.send_file(ctx.message.channel, './img/kawaii.jpg')


@client.command(pass_context=True, aliases=["/s, sar"])
async def sarcasm(ctx):
    """React to sarcasm"""
    await client.send_file(ctx.message.channel, './img/sarcasm.jpg')


@client.command(pass_context=True, aliases=["spoil"])
async def spoiler(ctx):
    """React to spoilers"""
    await client.send_file(ctx.message.channel, './img/spoiler.png')


async def kizuna(message):
    """React to kizuna name"""
    msg = await client.send_file(message.channel, './img/kizuna.png')     # Change the channel to our #kawaii


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    client.run(auth.discord_token)  # bot token

# This bot is built upon the Basic Bot template created by Habchy#1665
# Using discordpy's Discord API wrapper, and PRAW's reddit API wrapper
