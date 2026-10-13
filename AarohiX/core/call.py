
import asyncio
import importlib

from pyrogram import idle

import config
from AarohiX import LOGGER, app, userbot
from AarohiX.core.call import Dil
from AarohiX.misc import sudo
from AarohiX.plugins import ALL_MODULES
from AarohiX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if not any(
        [
            config.STRING1,
            config.STRING2,
            config.STRING3,
            config.STRING4,
            config.STRING5,
        ]
    ):
        LOGGER(__name__).error(
            "At least one assistant session (STRING1-STRING5) is required."
        )
        return

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        LOGGER(__name__).warning(
            "Could not load all banned-user records. Continuing startup."
        )

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("AarohiX.plugins" + all_module)

    LOGGER("AarohiX.plugins").info(
        "Successfully imported all modules."
    )

    await userbot.start()
    await Dil.start()

    # Logger-group voice-chat test removed.
    # A logger group/channel is not required to start the bot.

    await Dil.decorators()

    LOGGER("AarohiX").info(
        "Music bot started successfully."
    )

    await idle()

    await app.stop()
    await userbot.stop()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
