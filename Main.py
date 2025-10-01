import dotenv
import os
from async_ import *

#Discord Bot Token
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


#View for selection box in text channel
class MyView(discord.ui.View):
    @discord.ui.select(
        placeholder="Choose a command",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="New Campaign",
                description="Create a new campaign tied to this guild!"
            ),
            discord.SelectOption(
                label="Add Character",
                description="Add a character to the campaign!"
            ),
            discord.SelectOption(
                label="Add Weapon",
                description="Add a weapon to the campaign!"
            ),
            discord.SelectOption(
                label="Change Stat",
                description="Change the stats of specific weapons, characters, etc.!"
            ),
            discord.SelectOption(
                label="Encounter",
                description="Start an encounter with the current characters, and add NPC's/Bosses/Enemies!"
            ),
            discord.SelectOption(
                label="Find Stats",
                description="Find specific stats about a character or weapons!"
            )
        ]
    )
    #Communicates with Python perform functions
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        choice = select.values[0]
        if choice == "New Campaign":
            await new_campaign(interaction)
        if choice == "Add Character":
            await add_character(interaction)
        if choice == "Add Weapon":
            await add_weapon(interaction)
        if choice == "Find Stats":
            await find_weapons_(interaction)
        if choice == "Change Stats":
            await change_stats(interaction)
        if choice =="Encounter":
            await encounter(interaction)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_guild_join(guild):
    print(f'We have joined {guild.name}')
    await text_channel(guild)

@bot.command()
async def test_channel(ctx):
    guild = ctx.guild
    await text_channel(guild)

#Displays MyView List selection into Discord channel
@bot.command()
async def command_list(ctx):
    await ctx.send("Choose a command:", view=MyView())

bot.run(token)


