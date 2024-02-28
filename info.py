import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 9999))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://telegra.ph/file/56a0ea670f85e26e69226.jpg')).split()
NOR_IMG = environ.get('NOR_IMG', "https://graph.org/file/ebecf2e8bd05f866ea862.jpg")
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '<b><u>😻𝗛𝗲𝗹𝗹𝗼 {user},</u>\n\n𝗜 𝗺 𝗔 𝗠𝗼𝘃𝗶𝗲𝘀 𝗦𝗲𝗮𝗿𝗰𝗵 𝗕𝗼𝘁,𝗜𝗖𝗮𝗻 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗔𝗻𝗱 𝗪𝗘𝗕-𝗦𝗲𝗿𝗶𝗲𝘀,𝗝𝘂𝘀𝘁 𝗔𝗱𝗱 𝗠𝗲 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽𝘀 𝗔𝗻𝗱 𝗘𝗮𝗷𝗼𝘆..!</b>')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "👋𝗛𝗲𝗹𝗹𝗼 {query}!𝗧𝗵𝗮𝘁'𝘀 𝗡𝗼𝘁  𝗙𝗼𝗿  𝗬𝗼𝘂. 𝗣𝗹𝗲𝗮𝘀𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗬𝗼𝘂𝗿 𝗠𝗼𝘃𝗶𝗲..!!")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '<b>𝗙𝗶𝗿𝘀𝘁 𝗖𝗹𝗶𝗰𝗸 𝗢𝗻 "📢 𝗝𝗼𝗶𝗻 𝗨𝗽𝗱𝗮𝘁𝗲𝘀" 𝗕𝘂𝘁𝘁𝗼𝗻. 𝗧𝗵𝗲𝗻 𝗖𝗼𝗺𝗲 𝗕𝗮𝗰𝗸 𝗧𝗼 𝗧𝗵𝗲 𝗕𝗼𝘁 𝗔𝗻𝗱 𝗖𝗹𝗶𝗰𝗸 𝗢𝗻 "🔄𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻" 𝗕𝘂𝘁𝘁𝗼𝗻 𝗧𝗼 𝗚𝗲𝘁 𝗬𝗼𝘂𝗿 𝗠𝗼𝘃𝗶𝗲 𝗙𝗶𝗹𝗲𝘀.📂</b>')
WELCOM_PIC = environ.get("WELCOM_PIC", "https://telegra.ph/file/376d52c7273bb6451dac6.mp4")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "<b>🤍𝗛𝗲𝗹𝗹𝗼 {user} ░▒▓█\n\n𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼💞 {chat} 💞,\n𝗪𝗲 𝗣𝗿𝗼𝘃𝗶𝗱𝗶𝗻𝗴 𝗔𝗹𝗹 𝗠𝗼𝘃𝗶𝗲𝘀 & 𝗧𝗩 𝗦𝗲𝗿𝗶𝗲𝘀.\n\n😻 𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗝𝗼𝗶𝗻𝗶𝗻𝗴 😻</b>")
PMFILTER = bool(environ.get("PMFILTER", True))
G_FILTER = bool(environ.get("G_FILTER", True))
SUPPORT_CHAT_ID = -1001977093694
BUTTON_LOCK = bool(environ.get("BUTTON_LOCK", True))

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "9999"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'bot_support_chat_group')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', False))
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>🗂️𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 </b> :-: <b><code>{file_name}</code></b>\n<b>💎𝗙𝗶𝗹𝗲 𝗦𝗶𝘇𝗲 </b> :-: <b>{file_size}</b><b>\n🔖 𝗚𝗿𝗼𝘂𝗽 1 ➧ [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/+iEbhY7mM4oE1OTVl)🔖 𝗚𝗿𝗼𝘂𝗽 2 ➧ [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/Mallu_Movie_Hub_Group)📮 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ➧ [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/cinema_flix_updates)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>😻 𝗛𝗲𝘆 :-:</b> {message.from_user.mention},\n\n<b>🍿 𝗠𝗼𝘃𝗶𝗲 𝗡𝗮𝗺𝗲 :-:</b> <b>{title}</b>\n<b>🗂 𝗧𝗼𝘁𝗮𝗹 𝗙𝗶𝗹𝗲𝘀 :-:</b> <b>{str(total_results)}</b>\n<b>📅 𝗬𝗲𝗮𝗿 :-:</b> <b>{release_date}</b>\n<b>🔊 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 :-:</b> <b>{languages}</b>\n<b>⏳ 𝗚𝗲𝗻𝗿𝗲𝘀 :-:</b> <b>{genres}</b>\n<b>👍 𝗟𝗶𝗸𝗲𝗱 :-:</b> <b>{rating}</a> / 10</b>\n\n<b>🍃 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 :-:</b> <b>{message.chat.title}</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#log srt
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


