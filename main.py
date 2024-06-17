from __future__ import annotations

import logging
import os
from typing import Any, Optional

import discord
from discord.ext import commands
from dotenv import load_dotenv

from command_tree import JDCommandTranslator, JDCommandTree


class JDBot(commands.Bot):
    tree: JDCommandTree  # type: ignore

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        await self.tree.set_translator(JDCommandTranslator())


intents = discord.Intents.all()

bot = JDBot(
    command_prefix="h$",
    intents=intents,
    chunk_guilds_at_startup=False,
    strip_after_prefix=True,
    allowed_mentions=discord.AllowedMentions(everyone=False, roles=False),
)

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot.run(os.environ["TOKEN"])
