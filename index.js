const { Client, GatewayIntentBits, ChannelType } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildVoiceStates] });

const token = process.env.BOT_TOKEN;
const joinToCreateChannelId = process.env.JOINTOCREATE_CHANNEL_ID;

client.once('ready', () => {
    console.log('Ready!');
});

client.on('voiceStateUpdate', (oldState, newState) => {
    if (newState.channelId === joinToCreateChannelId) {
        newState.guild.channels.create({
            name: `🔊 ${newState.member.displayName}'s Channel`,
            type: ChannelType.GuildVoice,
            parent: newState.channel.parentId,
        }).then(channel => {
            newState.member.voice.setChannel(channel);
        }).catch(console.error);
    }

    if (oldState.channel && oldState.channel.members.size === 0 && oldState.channelId !== joinToCreateChannelId) {
        oldState.channel.delete().catch(console.error);
    }
});

client.login(token);
