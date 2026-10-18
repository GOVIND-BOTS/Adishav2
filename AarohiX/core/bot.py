
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

        # Logger notification is optional.
        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} bot started:</b></u>\n\n"
                    f"ID: <code>{self.id}</code>\n"
                    f"Name: {self.name}\n"
                    f"Username: @{self.username}"
                ),
            )
            LOGGER(__name__).info("Startup notification sent.")

        except Exception as error:
            LOGGER(__name__).warning(
                "Logger notification skipped (%s). "
                "Continuing without the logger group.",
                type(error).__name__,
            )

        LOGGER(__name__).info(
            "Bot authenticated successfully as %s", self.name
        )

    async def stop(self):
        await super().stop()
