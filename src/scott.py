from discord import Client, File, Embed, Colour
from dotenv import load_dotenv
from os import getenv

def scottify(message: str) -> str:
    scotty = ""
    for char in message:
        if char.isnumeric():
            scotty += char
        elif char.isalpha():
            scotty += char.lower()
    return scotty


client = Client()


@client.event
async def on_message(message):

    converted = scottify(message.content)
    print(converted)

    if "scott" in converted and "moe" in converted:
        with open("scott.gif", "rb") as f:
            gif = File(f)

        await message.channel.send(file=gif)

load_dotenv()

client.run(getenv('TOKEN'))
