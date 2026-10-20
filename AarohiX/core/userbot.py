```python
from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AarohiXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )

        self.two = Client(
            name="AarohiXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )

        self.three = Client(
            name="AarohiXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )

        self.four = Client(
            name="AarohiXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )

        self.five = Client(
            name="AarohiXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting assistant accounts...")

        accounts = [
            (1, self.one, config.STRING1),
            (2, self.two, config.STRING2),
            (3, self.three, config.STRING3),
            (4, self.four, config.STRING4),
            (5, self.five, config.STRING5),
        ]

        for number, client, session in accounts:
            if not session:
                continue

            try:
                await client.start()
                me = await client.get_me()

                client.username = me.username
                client.id = me.id
                client.name = (
                    f"{me.first_name} {me.last_name}"
                    if me.last_name
                    else me.first_name
                )

                if number not in assistants:
                    assistants.append(number)

                if me.id not in assistantids:
                    assistantids.append(me.id)

                LOGGER(__name__).info(
                    "Assistant %s started as %s (@%s)",
                    number,
                    client.name,
                    client.username or "no_username",
                )

            except Exception:
                LOGGER(__name__).exception(
                    "Assistant %s failed to start.", number
                )
                raise

    async def stop(self):
        for client in (
            self.one,
            self.two,
            self.three,
            self.four,
            self.five,
        ):
            try:
                if client.is_connected:
                    await client.stop()
            except Exception:
                LOGGER(__name__).exception(
                    "Error while stopping an assistant."
                )
```
