import asyncio
import importlib
import sys

# ========== FIX START ==========
# Event loop force create (Python 3.10+ ke liye zaroori)
if sys.version_info >= (3, 10):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()
# ========== FIX END ==========

from pyrogram import idle

import config
from AarohiX import LOGGER, app, userbot
from AarohiX.core.call import Dil
from AarohiX.misc import sudo
from AarohiX.plugins import ALL_MODULES
from AarohiX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # At least one assistant session is required for voice-chat playback.
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
            "No assistant session configured. Set at least one STRING1-STRING5."
        )
        return

    await sudo()

    # Load banned users from the database when available.
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception as exc:
        LOGGER(__name__).warning("Could not load banned users from database: %s", exc)

    app_started = False
    userbot_started = False

    try:
        await app.start()
        app_started = True

        for all_module in ALL_MODULES:
            importlib.import_module("AarohiX.plugins" + all_module)
        LOGGER("AarohiX.plugins").info("Successfully imported all plugin modules.")

        await userbot.start()
        userbot_started = True

        await Dil.start()

        # Logger-group startup test deliberately removed.
        await Dil.decorators()

        LOGGER("AarohiX").info("Music bot started successfully.")
        await idle()

    except Exception as e:
        LOGGER("AarohiX").error(f"Bot crashed with error: {e}")
        raise   # important: error dikhe logs me

    finally:
        # Properly stop PyTgCalls first
        try:
            await Dil.stop()
        except Exception as exc:
            LOGGER("AarohiX").warning("Error stopping PyTgCalls: %s", exc)

        if userbot_started:
            try:
                await userbot.stop()
            except Exception as exc:
                LOGGER("AarohiX").warning("Error stopping assistant client: %s", exc)

        if app_started:
            try:
                await app.stop()
            except Exception as exc:
                LOGGER("AarohiX").warning("Error stopping bot client: %s", exc)

        LOGGER("AarohiX").info("Music bot stopped.")


if __name__ == "__main__":
    try:
        asyncio.run(init())
    except KeyboardInterrupt:
        LOGGER("AarohiX").info("Bot stopped by user.")
    except Exception as e:
        LOGGER("AarohiX").error(f"Fatal error: {e}")
