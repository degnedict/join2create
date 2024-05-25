import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('BOT_TOKEN')
join_to_create_channel_id = int(os.getenv('JOINTOCREATE_CHANNEL_ID'))

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == join_to_create_channel_id:
        new_channel = await after.channel.guild.create_voice_channel(
            name=f"🔊 {member.display_name}'s Channel",
            category=after.channel.category,
            reason='Created by JoinToCreate bot'
        )
        await member.move_to(new_channel)

    if before.channel and len(before.channel.members) == 0 and before.channel.id != join_to_create_channel_id:
        if before.channel.name.startswith('🔊'):
            await before.channel.delete(reason='No members left in the bot-created channel')

bot.run(token)
