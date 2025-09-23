import dotenv
import discord
import os
from discord.ext import commands

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


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
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(f"You selected: {select.values[0]}", ephemeral=True)

@bot.command()
async def command_list(ctx):

    await ctx.send("Choose a command:", view=MyView())


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(token)


