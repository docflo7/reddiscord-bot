import settings
from discord.ext import commands
from tools import tools

class admin():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.check(tools.is_owner)
    async def setname(self, ctx, *arg):
        """Set the bot's username"""
        if len(arg) == 0:
            await self.client.say("I can't change my name if you don't give one !")
            return
        name = ' '.join(arg)
        await self.client.edit_profile(username=name)
        await self.client.say("Owner changed bot name to : " + name)
#        await self.client.say("Sorry " + ctx.message.author.mention + ", you don't have the permission for this")

    @commands.command(pass_context=True)
    @commands.check(tools.is_owner_or_lord)
    async def setnick(self, ctx, *arg):
        """Set the bot's nickname for this server"""
        if len(arg) == 0:
            await self.client.say("I can't change my nickname if you don't give one !\nUse 'empty' if you want to remove the present one")
            return
        name = ' '.join(arg)
        if name == 'empty':
            await self.client.change_nickname(ctx.message.server.me, None)
            await self.client.say("My nickname has been reset by " + ctx.message.author.name)
        else:
            await self.client.change_nickname(ctx.message.server.me, name)
            await self.client.say(ctx.message.author.name + " changed bot nickname to : " + name)

    @commands.command(pass_context=True)
    @commands.check(tools.is_owner)
    async def setavatar(self, ctx, *arg):
        """Set the bot's avatar"""
        if len(arg) == 0:
            await self.client.say("I can't change my avatar if you don't give one !\nUse 'empty' if you want to remove the present one")
            return
        avatar_url = arg[0]
        if avatar_url == 'empty':
            await self.client.edit_profile(avatar=None)
        else:
            req = urllib.request.Request(avatar_url, headers={'User-Agent' : "Magic Browser"})
            file = urllib.request.urlopen(req).read()
            await self.client.edit_profile(avatar=file)
            await self.client.say("Owner changed bot avatar")

    @commands.command(hidden=True)
    @commands.check(tools.is_owner_or_lord)
    async def switch(self, arg):
        """Enable / disable a command"""
        if arg is None:
            await self.client.say("```You need to tell me what command to switch```")
            return
        com = self.client.get_command(arg)
        if com is None:
            await self.client.say("No matching command found")
        else:
            com.enabled = not com.enabled
            status = 'enabled' if com.enabled else 'disabled'
            await self.client.say(com.name + " is now " + status)
            return

    @commands.command(name='whoami', hidden=True, pass_context=True)
    @commands.check(tools.is_owner)
    async def _me(self):
        await self.client.say("I'm " + str(self.client.user))


def setup(client):
    client.add_cog(admin(client))