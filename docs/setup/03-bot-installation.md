# Bot Installation

## Overview

BOT FC27 is a private Discord application developed for the
FC 27 Clubs Pro statistics project.

The application is currently used in a private Discord server
for development and testing.

## Discord Application

Application name:

`BOT FC27`

The application was created using the Discord Developer Portal.

## Installation Context

The application is configured for server installation only.

- Server installation: Enabled
- User installation: Disabled

## OAuth2 Scopes

The following OAuth2 scopes are configured:

- `bot`
- `applications.commands`

The `bot` scope allows the application to operate as a Discord bot.

The `applications.commands` scope allows the bot to use Discord
application commands such as `/ping`, `/club` and `/player`.

## Bot Permissions

The bot follows the principle of least privilege.

The following permissions were granted:

- View Channels
- Send Messages
- Embed Links

The Administrator permission was intentionally not granted.

## Security

The Discord bot token will not be stored directly in the source code.

The token will be stored using environment variables and a local
`.env` file.

The `.env` file will be excluded from version control.

## Installation

The bot was installed on a private Discord development server.

The bot currently appears as offline because the Python application
has not yet been connected to Discord.

## Screenshots

### OAuth2 Configuration

![OAuth2 configuration](../images/02-oauth2-permissions.png)

### Bot Installation

![Bot installed in Discord](../images/03-bot-installed.png)