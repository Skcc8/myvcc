##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN', "5929537401:AAF2jMjx2tQsojl3C5JxmQXcJ__RiRjuWqQ")
API_ID = int(getenv("API_ID", "22733485"))
API_HASH = getenv('API_HASH', "e6095dc075ad1ef78eb7697ece6d6feb")
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://userbot:userbot@cluster0.zcd4byg.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', "5843477713" ).split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001688479760'))
ASS_ID = int(getenv("ASS_ID", "5179814789"))
OWNER_ID = list(map(int, getenv('OWNER_ID', "5699529523" ).split()))
RESULT_PIC = getenv('RESULT_PIC', "https://te.legra.ph/file/38782fcbb44134010fba9.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://te.legra.ph/file/38782fcbb44134010fba9.jpg")
PING_IMG = getenv('PING_IMG', "https://te.legra.ph/file/38782fcbb44134010fba9.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
