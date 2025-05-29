import os
import asyncio
import random
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load config
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

config = load_config()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    auto_task.start()

@tasks.loop(seconds=10)
async def auto_task():
    await bot.wait_until_ready()
    channel = bot.get_channel(YOUR_CHANNEL_ID)  # Replace this with your actual channel ID
    if not channel:
        print("Channel not found. Check your channel ID.")
        return

    now = asyncio.get_event_loop().time()
    for cmd, entry in config.items():
        if entry["enabled"]:
            last = entry.get("last_run", 0)
            delay = random.randint(entry["min_delay"], entry["max_delay"])
            if now - last >= delay:
                await channel.send(f"rpg {cmd}")
                entry["last_run"] = now

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

@bot.command()
async def start(ctx):
    await ctx.send("Bot started! Commands will begin running.")

@bot.command()
async def stop(ctx):
    auto_task.cancel()
    await ctx.send("Bot stopped.")

@bot.command()
async def config_set(ctx, cmd, min_d: int, max_d: int, delay: int):
    if cmd in config:
        config[cmd] = {"enabled": True, "min_delay": min_d, "max_delay": max_d}
        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)
        await ctx.send(f"Config updated for {cmd}.")
    else:
        await ctx.send("Command not found in config.")

bot.run(TOKEN)