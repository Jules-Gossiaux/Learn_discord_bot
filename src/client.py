"""Application entry point for the educational Discord bot."""

from __future__ import annotations

import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

COMMAND_PREFIX = "!"
MAX_AUDIT_MESSAGE_LENGTH = 1_500

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("educational_discord_bot")


def build_intents() -> discord.Intents:
    """Return only the gateway intents required by this application."""

    intents = discord.Intents.default()
    intents.message_content = True
    return intents


def shorten_message(content: str) -> str:
    """Keep audit messages below Discord's message-length limit."""

    if len(content) <= MAX_AUDIT_MESSAGE_LENGTH:
        return content
    return f"{content[:MAX_AUDIT_MESSAGE_LENGTH - 3]}..."


class EducationalBot(commands.Bot):
    """Small, event-driven Discord bot used for learning purposes."""

    def __init__(self) -> None:
        super().__init__(
            command_prefix=COMMAND_PREFIX,
            intents=build_intents(),
            help_command=commands.DefaultHelpCommand(
                no_category="Commandes disponibles"
            ),
        )

    async def setup_hook(self) -> None:
        """Run startup hooks before connecting to Discord."""

        command_names = sorted(command.name for command in self.commands)
        logger.info("Bot commands loaded: %s", ", ".join(command_names))

    async def on_ready(self) -> None:
        """Log the successful connection to Discord."""

        if self.user is not None:
            logger.info("Connected as %s (id=%s)", self.user, self.user.id)

    async def on_command_error(
        self,
        context: commands.Context["EducationalBot"],
        error: commands.CommandError,
    ) -> None:
        """Handle expected command errors without crashing the bot."""

        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.MissingRequiredArgument):
            await context.send("Il manque un argument à cette commande.")
            return
        if isinstance(error, commands.CommandOnCooldown):
            await context.send(
                f"Réessaie dans {error.retry_after:.1f} seconde(s)."
            )
            return

        logger.exception("Unhandled command error", exc_info=error)
        await context.send("Une erreur inattendue est survenue.")


bot = EducationalBot()


@bot.command()
async def bonjour(context: commands.Context[EducationalBot]) -> None:
    """Reply to a friendly greeting."""

    await context.send(f"Bonjour {context.author.mention} !")


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def ping(context: commands.Context[EducationalBot]) -> None:
    """Return the bot's current WebSocket latency."""

    latency_ms = round(bot.latency * 1_000)
    await context.send(f"Pong ! Latence : {latency_ms} ms")


@bot.event
async def on_message(message: discord.Message) -> None:
    """Process commands while ignoring messages sent by bots."""

    if message.author.bot:
        return

    await bot.process_commands(message)


@bot.event
async def on_message_delete(message: discord.Message) -> None:
    """Announce deleted cached messages in their original channel."""

    if message.author.bot or message.guild is None:
        return

    content = shorten_message(message.content or "(contenu indisponible)")
    await message.channel.send(
        f"{message.author.mention} a supprimé ce message : {content}"
    )


@bot.event
async def on_message_edit(
    before: discord.Message,
    after: discord.Message,
) -> None:
    """Announce meaningful edits to cached messages."""

    if before.author.bot or before.guild is None or before.content == after.content:
        return

    old_content = shorten_message(before.content or "(vide)")
    new_content = shorten_message(after.content or "(vide)")
    await after.channel.send(
        f"{after.author.mention} a modifié son message :\n"
        f"Avant : {old_content}\nAprès : {new_content}"
    )


def main() -> None:
    """Start the bot and close the connection cleanly on interruption."""

    if not DISCORD_TOKEN:
        raise RuntimeError(
            "DISCORD_TOKEN is missing. Add it to a local .env file."
        )

    try:
        bot.run(DISCORD_TOKEN, log_handler=None)
    except discord.LoginFailure:
        logger.error("Discord rejected the configured token")
        raise
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")


if __name__ == "__main__":
    main()
