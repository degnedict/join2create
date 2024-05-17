# join2create

Join2Create is a Discord bot designed to facilitate JoinToCreate functionality seamlessly within your Discord channels.

## Getting Started

1. **Create a Discord Application**: Visit the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Make sure to grant the application sufficient permissions, preferably Administrator.

2. **Invite the Bot to Your Server**: After creating the application, invite the bot to your Discord server using the OAuth2 URL provided in the Discord Developer Portal.

3. **Configure Bot Parameters**:
    - Open `docker-compose.yml` and input your bot token and channel ID.
    - Alternatively, you can use the following Docker command:

    ```bash
    docker run -d \
      --name discord-bot \
      -e BOT_TOKEN=YOUR_BOT_TOKEN_HERE \
      -e JOINTOCREATE_CHANNEL_ID=YOUR_JOINTOCREATE_CHANNEL_ID_HERE \
      git.degnedict.de/bene/join2create:latest
    ```

    Or use the one-liner version:

    ```bash
    docker run -d --name discord-bot -e BOT_TOKEN=YOUR_BOT_TOKEN_HERE -e JOINTOCREATE_CHANNEL_ID=YOUR_JOINTOCREATE_CHANNEL_ID_HERE your-gitea-hub-username/discord-bot:latest
    ```
