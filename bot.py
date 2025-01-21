
#supposed to import discord library
import discord
import os
#import the dotenv library to load environment variables
from dotenv import load_dotenv

#set up intents
intents = discord.Intents.default()
intents.message_content = True

# Create a client instance with specified intents
client = discord.Client(intents=intents)

# Pretty sure this prints in console when you run the bot successfully
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# If a message starts with '!roll' it will respond with a message
@client.event
async def on_message(message):
    if message.author == client.user:   #if the message author is the bot itself, ignore it
        return

    if message.content.startswith('!roll'):
        await message.channel.send('What would you like to roll?')

# Put token here 
client.run(os.getenv("TOKEN"))
