import discord
import asyncio
from discord.ext import commands
from prompts import *
from validation import *


async def inputs_(interaction:discord.Interaction, prompt_list):
    await interaction.response.send_message(
        "Please answer the following correctly. (You can change it later if you make a mistake)", ephemeral=True)

    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel

    stats = {}

    for key, question in prompt_list:
        question_msg = await interaction.followup.send(question)
        try:
            msg = await interaction.client.wait_for('message', timeout=60.0, check=check)
            stats[key] = msg.content.strip()
            await question_msg.delete()
            await msg.delete()
        except asyncio.TimeoutError:
            await interaction.followup.send("Timed out! Restart with /command_list")
            return None

    stats["guildid"] = interaction.guild.id

    return stats

async def text_channel(guild):
    channel_name = "Dazed_Tool_Bot"

    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        new_channel = await guild.create_text_channel(channel_name)
        await new_channel.send("Thank you for adding me to your server! Type /command_list to get started.")

async def new_campaign(interaction: discord.Interaction):
    id = (interaction.guild.id, interaction.guild.name)
    executequery(id,add_campaign)
    await interaction.response.send_message("Campaign successfully started", ephemeral=True)

async def add_character(interaction: discord.Interaction):
    stats = await inputs_(interaction, character_)
    if stats is None:
        return
    statement = char_insert
    executequery(stats,statement)
    await interaction.followup.send("Character successfully added!", ephemeral=True)

async def add_weapon(interaction: discord.Interaction):
    stats = await inputs_(interaction,weapon_)
    if stats is None:
        return
    executequery(stats,weapon_insert)
    await interaction.followup.send("Weapon successfully added", ephemeral=True)

async def change_stats(interaction: discord.Interaction):
    await interaction.response.send_message("Campaign successfully started", ephemeral=True)

async def encounter(interaction: discord.Interaction):
    temp = (interaction.guild.id,)
    fetch = True
    message = executequery(temp, get_characters,fetch)
    for character in message:
        formatted = f"{character}! Take your turn!"

    await interaction.response.send_message(f"{formatted}", ephemeral=True)

async def find_weapons_(interaction: discord.Interaction):

    temp = (interaction.guild.id,)
    fetch = True
    message = executequery(temp, get_weapons, fetch)
    formatted = ""
    print(message)
    for weapon in message:
        name, cost, damage, weight, properties, type_, guild_id = weapon
        formatted += (
            f"**Name:** {name}\n"
            f"• Cost: `{cost}`\n"
            f"• Damage: `{damage}`\n"
            f"• Weight: `{weight}`\n"
            f"• Properties: `{properties}`\n"
            f"• Type: `{type_}`\n\n"
        )

    await interaction.response.send_message(f"__**Weapons:**__\n{formatted}", ephemeral=True)