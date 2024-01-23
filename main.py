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

async def madu(message: discord.Message) -> None:
    if (message.author.id not in [1157141134376697968, 1111020727425060905]):
        return
        

    for word in bot.config['delusions']:
        delusion = rf'\b{word}s?\b'
        if (re.search(delusion, message.content, re.IGNORECASE)):
            # await message.channel.send("<:sus2:1194168202989682729>", reference=message)
            await message.channel.send("[find god](https://www.amazon.com/Church-Bible-Black-Bibles-Crossway/dp/1433563428/ref=asc_df_1433563428/?tag=hyprod-20&linkCode=df0&hvadid=312748656151&hvpos=&hvnetw=g&hvrand=4269571702995196639&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9012067&hvtargid=pla-525321634691&psc=1&mcid=7756fdba02a43bd89b0248b9dc9aea06&gclid=Cj0KCQiAnrOtBhDIARIsAFsSe530XtUA10NRrFwXgWSQXL3tSc1r65IID_NPuip3dMDL537e5khSn3saAqCdEALw_wcB)", reference=message)
            break

async def lockin(message: discord.Message) -> None:
    if (message.author.id not in [716825633530839101, 363700491093409793, 1117664729725419550]):
        return
    
    pattern1 = rf'lock'
    pattern2 = rf'not'
    # If word has the word 'lock' in it but not 'not'
    if (re.search(pattern1, message.content, re.IGNORECASE) and not re.search(pattern2, message.content, re.IGNORECASE)):
        await message.channel.send("<:sus2:1194168202989682729>", reference=message)

@bot.event
async def on_message(message: discord.Message) -> None:
    await madu(message)
    await lockin(message)
    await bot.process_commands(message)



bot.run(os.getenv("TOKEN"))
