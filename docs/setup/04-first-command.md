# First Discord Command

## Overview

The first functional command implemented in the FC27 Clubs Discord Bot
is `/ping`.

The command was created to verify that the Python application can
receive Discord interactions and respond successfully.

## Command

`/ping`

## Response

`🏓 Pong!`

## Implementation

The command was implemented using the Discord application command
system provided by `discord.py`.

The command is registered using a `CommandTree` and synchronized
with Discord when the bot starts.

## Validation

The command was successfully executed from the development Discord
server and returned the expected response.

## Screenshot

![Ping command](../images/04-ping-command.png)