import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

language_commands = {
    'en': {
        'info': "This is information in English.",
        'githubproj': "We don't hide any information about our bot. The entire code and all the necessary files are available in our [GitHub repository](https://github.com/straz1ki/vipus.project).",
        'about_gw': "Global warming is the long-term increase in Earth's average surface temperature, mainly caused by human activities like burning fossil fuels. It leads to climate changes, extreme weather events, and rising sea levels.",
        'fields': {
            'contribute': "If you're unsure about how to contribute to the well-being of our planet, our bot is here to assist you! We'll use memes to enhance your understanding of environmental information.",
            'other_info': "blah blah blah"
        },
        'footer': "Eco-System Bot administ."
    },
    'ru': {
        'info': "Это информация на русском.",
        'githubproj': "Мы не скрываем никакой информации о нашем боте. Весь код, все нужные файлы есть в нашем [репозитории GitHub](https://github.com/straz1ki/vipus.project). Если вы хотите получше ознакомиться, нажмите сюда.",
        'about_gw': "Глобальное потепление - это долгосрочное увеличение средней поверхностной температуры Земли, в основном вызванное деятельностью человека, такой как сжигание ископаемых топлив. Это приводит к изменениям климата, экстремальным погодным явлениям и поднятию уровня морей.",
        'fields': {
            'contribute': "Если вы не уверены, как внести вклад в благополучие нашей планеты, наш бот здесь, чтобы вам помочь! Мы используем мемы, чтобы улучшить ваше понимание экологической информации.",
            'other_info': "бла бла бла"
        },
        'footer': "Администрация Eco-System Bot"
    }
}

user_languages = {}

bot.user_command_counts = {}


roles_for_commands = {
    10: "1182937460045512814",
    20: "1182937458720129035",
    30: "1182937447206760478"

}

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

    repository_link = "[Repository](https://github.com/straz1ki/vipus.project)"
    embed.description += f"\n{repository_link}"

    await ctx.send(embed=embed)

@bot.command()
async def about_gw(ctx):
    user_language = user_languages.get(ctx.author.id, 'en')
    language_info = language_commands[user_language]['about_gw']

    embed = discord.Embed(
        title="What is Global warming?",
        description=language_info,
        color=discord.Color.blue()
    )
    embed.add_field(name="Interesting Fact", value="Polar Amplification: One intriguing aspect of global warming is the phenomenon of polar amplification. The Arctic is warming at about twice the global average rate, leading to faster ice melt and significant ecological changes in this region.")
    embed.set_footer(text="Eco-System Bot administ.")
    
    image_path = "/Users/aray/Downloads/YEAHAHAH/meme-1.jpg"
    embed.set_image(url=f"attachment://meme-1.jpg")

    with open(image_path, "rb") as image_file:
        await ctx.send(embed=embed, file=discord.File(image_file, "meme-1.jpg"))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    user_id = str(message.author.id)
    if user_id not in bot.user_command_counts:
        bot.user_command_counts[user_id] = 0
    bot.user_command_counts[user_id] += 1

    for command_count, role_id in roles_for_commands.items():
        if bot.user_command_counts[user_id] == command_count:
            role = discord.utils.get(message.guild.roles, id=role_id)
            if role:
                await message.author.add_roles(role)
                await message.channel.send(f'Congratulations! You have been awarded the role with ID {role_id} for reaching {command_count} command uses.')

bot.run('token')
