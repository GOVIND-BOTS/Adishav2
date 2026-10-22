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


async def main():
    app_started = False
    userbot_started = False
    calls_started = False

    try:
        if not any(
            [
                config.STRING1,
                config.STRING2,
                config.STRING3,
                config.STRING4,
                config.STRING5,
            ]
        ):
            LOGGER("AarohiX").error(
                "No assistant session configured. Set STRING_SESSION."
            )
            return

        await sudo()

        try:
            for user_id in await get_gbanned():
                BANNED_USERS.add(user_id)

            for user_id in await get_banned_users():
                BANNED_USERS.add(user_id)
        except Exception:
            LOGGER("AarohiX").warning(
                "Could not load banned users.", exc_info=True
            )

        await app.start()
        app_started = True
        LOGGER("AarohiX").info("Bot client started.")

        for module in ALL_MODULES:
            importlib.import_module("AarohiX.plugins" + module)

        LOGGER("AarohiX").info("Plugin modules loaded.")

        await userbot.start()
        userbot_started = True
        LOGGER("AarohiX").info("Userbot started.")

        await Dil.start()
        calls_started = True
        await Dil.decorators()

        LOGGER("AarohiX").info("Music bot started successfully.")
        await idle()

    except asyncio.CancelledError:
        raise
    except Exception:
        LOGGER("AarohiX").error(
            "Startup/runtime error.", exc_info=True
        )
        raise
    finally:
        # 1. Pehle voice calls band karo
        if calls_started:
            try:
                await Dil.stop()
            except Exception:
                LOGGER("AarohiX").warning(
                    "Error stopping voice-call clients.", exc_info=True
                )

        # 2. Userbot band karo
        if userbot_started:
            try:
                await userbot.stop()
            except Exception:
                LOGGER("AarohiX").warning(
                    "Error stopping userbot.", exc_info=True
                )

        # 3. Bot client band karo
        if app_started:
            try:
                await app.stop()
            except Exception:
                LOGGER("AarohiX").warning(
                    "Error stopping bot client.", exc_info=True
                )

        # 4. Pending tasks clean karo (error kam karne ke liye)
        try:
            tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
            for task in tasks:
                task.cancel()
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
        except Exception:
            pass

        LOGGER("AarohiX").info("Shutdown complete.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    except Exception:
        # The actual traceback is logged inside main().
        pass
