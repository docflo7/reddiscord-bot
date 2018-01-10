#This file is the template for file auth.py
#It contains the authentication data used by the bot
#Feel free to remove the comments once you have edited this file
#And don't forget to rename it to auth.py

def init():
    global discord_command_prefix
    global discord_token
    global reddit_client
    global reddit_secret
    global db_name
    global db_host
    global db_port
    global db_user
    global db_pass

	"""Discord related datas"""
    discord_command_prefix = ''	#The prefix used by the bot, to call the commands
    discord_token = ''			#Your bot token. If you don't know what this is about, visit https://github.com/Habchy/BasicBot and follow Habchy#1665 explanations
    
	"""reddit related datas"""
	reddit_client = ''			#Your reddit app client id												
    reddit_secret = ''			#Your reddit app secret						
    
	"""Postgres database related datas"""
	db_name = ''				#Database name						
    db_host = ''				#Database host 											
    db_port = ''				#Database port												
    db_user = ''				#Database username											
    db_pass = ''				#Database password										