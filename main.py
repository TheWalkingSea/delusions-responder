import discord
from discord.ext import commands
import json
import aiofiles
import re
from dotenv import load_dotenv
import os


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")
    async with aiofiles.open("config.json", mode="rb") as f:
        bot.config = json.loads((await f.read()))


@bot.event
async def on_message(message: discord.Message) -> None:
    if (message.author.id not in [1157141134376697968, 1111020727425060905]):
        await bot.process_commands(message)
        return
        

    for word in bot.config['delusions']:
        delusion = rf'\b{word}[\bs]'
        if (re.search(delusion, message.content, re.IGNORECASE)):
            await message.channel.send("<:sus2:1194168202989682729>", reference=message)
            break

    await bot.process_commands(message)



bot.run(os.getenv("TOKEN"))