import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

RUN = list(map(int, getenv("RUN", "8250224070").split()))
