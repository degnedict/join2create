# join2create

A simple Discord Bot to provide JoinToCreate functionality.
Create your Application and give the bot sufficient permissions (i gave id Admin).

Put your Bot Key and your Channel ID in the docker-compose.yml or use this command
```docker run -d \
  --name discord-bot \
  -e BOT_TOKEN=YOUR_BOT_TOKEN_HERE \
  -e JOINTOCREATE_CHANNEL_ID=YOUR_JOINTOCREATE_CHANNEL_ID_HERE \
  git.degnedict.de/bene/join2create:latest```