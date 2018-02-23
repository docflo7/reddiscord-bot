# reddiscord-bot
A discord bot posting pictures from anime subreddits

## Installation  
To use this discord bot, you will need : 
- Python 3.X
- A discord bot account. You can follow [these](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) instructions to get one.  
- A reddit app. You can learn more about it [here](http://pythonforengineers.com/build-a-reddit-bot-part-1/) 
- A postgres database. 

To install the required packages, run :  
```pip install discord.py praw psycopg2 apscheduler```  
if discord.py package installation fails, clone [the repository](https://github.com/Rapptz/discord.py) and run `setup.py`  

You will need to create an `auth.py` file, using the `auth_template.py`, containing the authentication informations  

Then, you can run `reddiscord.core.py` to run the bot  

## Configuration
For now, the settings are limited.  
You can chose which extensions from the bot you would like to load on startup (These can still be loaded/unloaded afterward). To do this, edit `startup_extensions` from `settings.py`

## Extensions & Commands
The commands are split in differents extensions.  
You can use the `help` command to get more infos about each command

### Admin  
This extensions contains commands related to the bot administration.  
Most are limited to the bot owner or the server owner.  

- setname : to set the bot name | Bot owner only
- setnick : to set the bot nickname | Bot and server owner
- setavatar : to change the bot avatar (using an url)| Bot owner only
- switch : to switch a command on/off | Bot and server owner

### SFW
This extension contains commands related to sfw anime subreddits.
- aww : r/awwnime (kawaii is an alias)
- fang : r/cutelittlefangs
- ponytail : r/animeponytails
- pout : r/pouts
- tsundere : r/Tsunderes

### NSFW
This extension contains commands related to nsfw anime subreddits.
- ecchi : r/ecchi
- flat : r/chiisaihentai
- hentai : r/hentai
- legwear : r/animelegwear
- nekogirl : r/Nekogirls
- nekomimi : r/Nekomimi
- pantsu : r/pantsu
- sukebei : r/Sukebei
- thh : r/thighhighhentai
- twintails : r/
- zr : r/ZettaiRyouiki

### Core commands
In the main program, there are a few useful commands.
- reload : to reload (or to load) an extension
- unload : to unload an extension
- remindme : a group of command to send reminders via pm

