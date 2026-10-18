
from pyrogram import Client

import config

from ..logging import LOGGER


class Dil(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")

        super().__init__(
            name="AarohiX",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # No logger group required.
        LOGGER(__name__).info(
            "Bot authenticated successfully as %s", self.name
        )

    async def stop(self):
        await super().stop()
