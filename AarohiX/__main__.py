import asyncio
import importlib
import sys

# Force event loop early
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

from pyrogram import idle

import config
from AarohiX import LOGGER, app, userbot
from AarohiX.core.call import Dil
from AarohiX.misc import sudo
from AarohiX.plugins import ALL_MODULES
from AarohiX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if not any([
        config.STRING1,
        config.STRING2,
        config.STRING3,
        config.STRING4,
        config.STRING5,
    ]):
        LOGGER(__name__).error(
            "No assistant session configured. Set at least one STRING1-STRING5."
        )
        return

    await sudo()

    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception as exc:
        LOGGER(__name__).warning("Could not load banned users: %s", exc)

    try:
        await app.start()
        LOGGER("AarohiX").info("Bot client started.")

        for all_module in ALL_MODULES:
            importlib.import_module("AarohiX.plugins" + all_module)
        LOGGER("AarohiX.plugins").info("Successfully imported all plugin modules.")

        await userbot.start()
        LOGGER("AarohiX").info("Userbot started.")

        await Dil.start()
        await Dil.decorators()

        LOGGER("AarohiX").info("Music bot started successfully.")
        await idle()

    except Exception as e:
        LOGGER("AarohiX").error(f"Error while starting: {e}", exc_info=True)
        raise

    finally:
        try:
            await Dil.stop()
        except:
            pass
        try:
            await userbot.stop()
        except:
            pass
        try:
            await app.stop()
        except:
            pass
        LOGGER("AarohiX").info("Music bot stopped.")


if __name__ == "__main__":
    try:
        loop.run_until_complete(init())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        LOGGER("AarohiX").error(f"Fatal error: {e}", exc_info=True)
    finally:
        try:
            loop.close()
        except:
            pass
