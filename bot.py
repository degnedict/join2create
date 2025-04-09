import os
import json
import discord
import random  # hinzugefügt
from discord.ext import commands

DATA_FILE = "data/channel_data.json"

# Lade Trick-Namen aus der JSON-Datei im config-Ordner
try:
    with open(os.path.join(os.path.dirname(__file__), "config", "channelnames.json"), "r") as f:
        TRICK_NAMES = json.load(f)
except FileNotFoundError:
    TRICK_NAMES = ["Default Trick"]

def load_created_channels():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return set(data.get("created_channels", []))
    except FileNotFoundError:
        return set()

def save_created_channels(channels: set):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump({"created_channels": list(channels)}, f)

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('BOT_TOKEN')
join_to_create_channel_id = int(os.getenv('JOINTOCREATE_CHANNEL_ID'))

created_channels = load_created_channels()

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == join_to_create_channel_id:
        trick_name = random.choice(TRICK_NAMES)  # zufälliger Trick-Name
        new_channel = await after.channel.guild.create_voice_channel(
            name=f"🔊 {trick_name}",
            category=after.channel.category,
            reason='Created by JoinToCreate bot'
        )
        created_channels.add(new_channel.id)
        save_created_channels(created_channels)
        await member.move_to(new_channel)

    if before.channel and len(before.channel.members) == 0 and before.channel.id != join_to_create_channel_id:
        if before.channel.id in created_channels:
            await before.channel.delete(reason='No members left in the bot-created channel')
            created_channels.remove(before.channel.id)
            save_created_channels(created_channels)

bot.run(token)
