from discord import Client, File
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

        scott = converted.index("scott")
        moe = converted.index("moe")

        if scott < moe:
            with open("scott.gif", "rb") as f:
                gif = File(f)

        else:
            with open("ttocs.gif", "rb") as f:
                gif = File(f)

        await message.channel.send(file=gif)


# Load from any .env files
load_dotenv()

# Run the bot, where the bot token is probably stored in a .env file
client.run(getenv('TOKEN'))
