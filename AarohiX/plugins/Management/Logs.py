from pyrogram import Client, filters
from AarohiX.core.userbot import Userbot
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app

try:
    from config import LOGGER_ID as LOG_ID
except ImportError:
    LOG_ID = 0

userbot = Userbot()


async def new_message(chat_id: int, message: str, reply_markup=None):
    if not chat_id or chat_id == 0:
        return
    try:
        await app.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
    except Exception:
        pass


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "Private"
        chat_id = message.chat.id

        text = f"✫ <b><u>ɴᴇᴡ ɢʀᴏᴜᴘ</u></b> :\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\nᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ : {username}\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\n\nᴀᴅᴅᴇᴅ ʙʏ : {added_by}"

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(message.from_user.first_name, user_id=message.from_user.id)]
        ])

        await new_message(LOG_ID, text, reply_markup)


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "Private"
        chat_id = message.chat.id

        text = f"✫ <b><u>ʟᴇғᴛ ɢʀᴏᴜᴘ</u></b> :\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\nᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ : {username}\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\n\nʀᴇᴍᴏᴠᴇᴅ ʙʏ : {remove_by}"

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(message.from_user.first_name, user_id=message.from_user.id)]
        ])

        await new_message(LOG_ID, text, reply_markup)

        try:
            await userbot.one.start()
            await userbot.one.leave_chat(chat_id)
        except Exception:
            pass
