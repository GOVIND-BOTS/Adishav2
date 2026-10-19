import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "28811345"))

API_HASH = getenv("API_HASH", "8df803a8832e85ddddcd8c05fe840a05")

BOT_TOKEN = getenv("BOT_TOKEN", "8695998901:AAHS0KRWOlZ2DCZj_AbiE1d1kcOtLbDl8dA")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://DxLEGEND143:DxLEGEND143@dxlegend.oztipqk.mongodb.net/?retryWrites=true&w=majority&appName=DxLEGEND")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)


OWNER_ID = int(getenv("OWNER_ID", "8250224070"))

BOT_USERNAME = getenv("BOT_USERNAME" , "@Testing_musicv3bot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/GOVIND-BOTS/Adishav2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/govind_official_mp13")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/govind_official_mp13")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session  
STRING1 = getenv("STRING_SESSION", "BQCZzqEAtGbd60ED05sMk4XtsP7GpOTMikiz-wY0BDzeTfpTevxdw_4DQ7bgmpn6x3Y_7sQ6hNGVHlHxmEbC2JG6YooX4Kog1nXVgwl57nqNUsgGEo-SwTpT_wR85w8lyLBTwsOoC_fIDjmW86taN-V3TK1iXaRk7k5Dng8YVuWdMEgjZLtN9_yB9Uy9o3ce48-IkNbijqccZIbaNteIXA8DkDEv_mStosi2YwKKn7A1wFTIZCNu_EpgKL-XIDn-z0crnA9-FQfqG7H3lAOqTcmed-hktFb2Fc4kByHKy6cPHi6sbnNsNWsHY1dhXlBou2cv08C0AxNwGVdL0_xn6xkMD0RFAAAAAAHrwG3GAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/c3bdae6f5f36d12c9e09a.mp4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/039d9913f90dffeb5835b.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/039d9913f90dffeb5835b.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/7af55a67398d46b4092a2.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/810f874873e1565cf5732.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/16d7dd76f4ce8b8b01fdf.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/039d9913f90dffeb5835b.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/664c5f7bfcd9b197f02cd.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
