
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus

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

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )

        except Exception:
            LOGGER(__name__).exception(
                "Failed to send startup message to the log group/channel. "
                "Check LOGGER_ID, chat access, and bot permissions."
            )
            raise

        try:
            member = await self.get_chat_member(
                config.LOGGER_ID,
                self.id,
            )

            if member.status not in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ):
                LOGGER(__name__).error(
                    "The bot must be an administrator in the log group/channel."
                )
                raise RuntimeError(
                    "Bot is not an administrator in the log group/channel."
                )

        except Exception:
            LOGGER(__name__).exception(
                "Failed to verify bot administrator status in the log group/channel."
            )
            raise

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
