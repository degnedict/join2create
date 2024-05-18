import os
import discord
from discord.ext import commands

# Konfiguriere die Bot-Instanz
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Bot-Token und Kategorie-IDs aus Umgebungsvariablen
TOKEN = os.getenv('BOT_TOKEN')
CATEGORY_IDS = os.getenv('CATEGORY_IDS').split(',')
JOINTOCREATE_CHANNEL_NAME = os.getenv('JOINTOCREATE_CHANNEL_NAME', 'Join to Create')

# Liste zur Speicherung der erstellten Kanäle
created_channels = []
join_to_create_channels = []

@bot.event
async def on_ready():
    print('Bot is ready!')

    # Erstellen der JoinToCreate-Kanäle in den angegebenen Kategorien
    for category_id in CATEGORY_IDS:
        category = bot.get_channel(int(category_id))
        join_to_create_channel = await category.create_voice_channel(name=JOINTOCREATE_CHANNEL_NAME)
        join_to_create_channels.append(join_to_create_channel.id)
        print(f'JoinToCreate Channel created in category {category_id} with ID: {join_to_create_channel.id}')

@bot.event
async def on_voice_state_update(member, before, after):
    global created_channels

    # Prüfen, ob der Benutzer in einen JoinToCreate-Kanal wechselt
    if after.channel and after.channel.id in join_to_create_channels:
        # Erstelle einen neuen Sprachkanal
        category = after.channel.category
        new_channel = await category.create_voice_channel(name=f'🔊 {member.display_name}\'s Channel')
        await member.move_to(new_channel)

        # Markiere den Kanal als vom Bot erstellt
        created_channels.append(new_channel.id)

    # Prüfen, ob ein Kanal leer geworden ist und ob er vom Bot erstellt wurde
    if before.channel and before.channel.id in created_channels and len(before.channel.members) == 0:
        await before.channel.delete()
        created_channels.remove(before.channel.id)

# Starte den Bot
bot.run(TOKEN)
