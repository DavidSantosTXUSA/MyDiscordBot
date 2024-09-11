import discord
from discord.ext import commands

# Intents are required for handling messages and other events
intents = discord.Intents.default()
intents.message_content = True

# Define bot prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# List to store banned words
banned_words = []

# Event when bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Command to add a word to the banned list (Admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def banword(ctx, *, word: str):
    banned_words.append(word.lower())
    await ctx.send(f'Added "{word}" to the banned words list.')

# Command to remove a word from the banned list (Admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def unbanword(ctx, *, word: str):
    if word.lower() in banned_words:
        banned_words.remove(word.lower())
        await ctx.send(f'Removed "{word}" from the banned words list.')
    else:
        await ctx.send(f'"{word}" is not in the banned words list.')

# Command to view the banned words list (Admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def bannedlist(ctx):
    if banned_words:
        await ctx.send(f'Banned words: {", ".join(banned_words)}')
    else:
        await ctx.send('No banned words yet.')

# Monitor messages for banned words
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message contains any banned word
    for word in banned_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f'{message.author.mention}, that word is not allowed!')
            return

    await bot.process_commands(message)

# Start the bot REAL TOKEN NOT SHOWN FOR SECURITY REASONS
bot.run('TOKEN_HERE')


