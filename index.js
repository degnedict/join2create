const { Client, GatewayIntentBits, ChannelType } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildVoiceStates] });

const token = process.env.BOT_TOKEN;
const joinToCreateChannelId = process.env.JOINTOCREATE_CHANNEL_ID;

// Set to true if a channel was created by the bot
const CREATED_BY_BOT = 'created_by_bot';

client.once('ready', () => {
    console.log('Ready!');
});

client.on('voiceStateUpdate', (oldState, newState) => {
    if (newState.channelId === joinToCreateChannelId) {
        newState.guild.channels.create({
            name: `🔊 ${newState.member.displayName}'s Channel`,
            type: ChannelType.GuildVoice,
            parent: newState.channel.parentId,
            reason: 'Created by JoinToCreate bot', // Add a reason when creating the channel
        }).then(channel => {
            newState.member.voice.setChannel(channel);
            channel[CREATED_BY_BOT] = true; // Mark the channel as created by the bot
        }).catch(console.error);
    }

    if (oldState.channel && oldState.channel.members.size === 0 && oldState.channel.id !== joinToCreateChannelId) {
        // Check if the channel was created by the bot before deleting it
        if (oldState.channel[CREATED_BY_BOT]) {
            oldState.channel.delete().catch(console.error);
        }
    }
});

client.login(token);
