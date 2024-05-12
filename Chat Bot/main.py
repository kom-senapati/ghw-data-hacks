# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os
from chat import get_response

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith("?"):
        return

    if message.content.startswith("?chatbot"):
        response = get_response(message.content[8:])
        await message.channel.send(response)

    elif message.content.startswith("?about"):
        await message.channel.send(
            "I am a chatbot created by @komsenapati. I am here to help you with your queries."
        )

    elif message.content.startswith("?help"):
        await message.channel.send(
            "You can ask me anything. Just type ?chatbot followed by your query."
        )

    elif message.content.startswith("?ping"):
        await message.channel.send("Pong!")


client.run(TOKEN)
