# Discord Moderation Bot

A simple Discord bot built with Python and Discord.py that allows server administrators to manage a list of banned words. The bot will automatically delete any messages containing banned words

## Features

- Add, remove, and view banned words (admin-only commands).
- Automatically deletes messages that contain banned words.
- Alerts users when their message contains a banned word.
- Simple and easy to configure.

## Commands

- `!banword <word>`: Adds a word to the banned list (Admin-only).
- `!unbanword <word>`: Removes a word from the banned list (Admin-only).
- `!bannedlist`: Displays the current list of banned words (Admin-only).
