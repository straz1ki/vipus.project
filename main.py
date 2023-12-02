import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)


language_commands = {
    'en': {
        'info': "This is information in English.",
        'githubproj': "We don't hide any information about our bot. The entire code and all the necessary files are available in our [GitHub repository](https://github.com/straz1ki/vipus.project).",
        'fields': {
            'contribute': "If you're unsure about how to contribute to the well-being of our planet, our bot is here to assist you! We'll use memes to enhance your understanding of environmental information.",
            'other_info': "blah blah blah"
        },
        'footer': "Eco-System Bot administ."
    },
    'ru': {
        'info': "Это информация на русском.",
        'githubproj': "Мы не скрываем никакой информации о нашем боте. Весь код, все нужные файлы есть в нашем [репозитории GitHub](https://github.com/straz1ki/vipus.project). Если вы хотите получше ознакомиться, нажмите сюда.",
        'fields': {
            'contribute': "Если вы не уверены, как внести вклад в благополучие нашей планеты, наш бот здесь, чтобы вам помочь! Мы используем мемы, чтобы улучшить ваше понимание экологической информации.",
            'other_info': "бла бла бла"
        },
        'footer': "Администрация Eco-System Bot"
    }
}

user_languages = {}

# online_status
@bot.event
async def on_ready():
    print(f'{bot.user} is online now.')

@bot.command()
async def setlanguage(ctx, language: str):
    if language.lower() in language_commands:
        user_languages[ctx.author.id] = language.lower()
        await ctx.send(f"Your language preference has been set to {language.lower()}.")
    else:
        await ctx.send(f"Invalid language. Please choose from: {', '.join(language_commands.keys())}.")

# all_commands
@bot.command()
async def info(ctx):
    user_language = user_languages.get(ctx.author.id, 'en')
    language_info = language_commands[user_language]['info']
    contribute_field = language_commands[user_language]['fields']['contribute']
    other_info_field = language_commands[user_language]['fields']['other_info']
    footer = language_commands[user_language]['footer']

    embed = discord.Embed(
        title="Eco-System Bot",
        description=language_info,
        color=discord.Color.green()
    )
    embed.add_field(name="How to Contribute", value=contribute_field)
    embed.add_field(name="Other Info", value=other_info_field)
    embed.set_footer(text=footer)

    await ctx.send(embed=embed)

@bot.command()
async def githubproj(ctx):
    user_language = user_languages.get(ctx.author.id, 'en')
    language_info = language_commands[user_language]['githubproj']

    embed = discord.Embed(
        title="Open Source Code",
        description=language_info,
        color=discord.Color.blue()
    )
    embed.add_field(name="Other Info", value="blah blah blah")
    embed.set_footer(text="Eco-System Bot administ.")

    await ctx.send(embed=embed)

bot.run('token')
