##MS-TAMIL-BOTZ
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'BQFtQlEACXiIiZGt7ClQ2WIKgZpBnDYBoMQofDTgrDQVODCAhZT9siUirCuN3eZDetpW_1E3U1vu8WGdy3kIf6Hnxu-Ozn00hh7b6-lW2EiMSFRuptA8iW44l165wJNUJl3yurVOzXmn8YPT73ylrvAdgs4SgCb3EpwGEotEE0jD1WfHdkCVkFDEE4X_kp73N3c_jtrJL2Gxyvh_5bb5XL-6CHA-ZXf2givQtrdDjjJd6Bgu5MbsWHBc8XYOrSvPv4QNh81PuzWhHJ24Ii25i0DsJuVPNjsytQJmcSxix0W8T2vMh0u6x4ZEtDXpDThzXfwQAufvcM6Ac6aHHH2epRypDr62hwAAAAFN_5jFAA')
API_ID = int(environ.get('API_ID', '23937617'))
API_HASH = environ.get('API_HASH', 'cdc408c8bf00c9c2219fee9cd585bbda')
BOT_TOKEN = environ.get('BOT_TOKEN', "5480894070:AAGOulqbcNjpspFxsXkprI8fIZvZVIWQ5XE")

#Port
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/68d28011b2bc356b5db01.png')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1412758888').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001502435182').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://OximeStorage:OximeStorage@cluster0.71k2bsv.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "OximeStorage")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001637312289'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '-1001597895790')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [TN 68 FILM FACTORY](https://t.me/TN68_FilmFactory)</b>⚡\n\nName: {file_caption} \n\n⚙️ <b>Size: </b><code>{file_size}</code>🔥  ↭ <b>Join Now [TN 68 FILM FACTORY](https://t.me/TN68_FilmFactory)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "⚡<b>File uploaded by [TN 68 FILM FACTORY](https://t.me/TN68_FilmFactory)</b>⚡\n\nName: {file_caption} \n\n⚙️ <b>Size: </b><code>{file_size}</code>🔥  ↭ <b>Join Now [TN 68 FILM FACTORY](https://t.me/TN68_FilmFactory)</b> ↭  🔥")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb: \n\n🏷 Title: {title}\n🌟 Rating : {rating}/10\n🎭 Genres: {genres}\n📆 Year: {year}\n⏰ Duration : {runtime}\n🎙️ Languages : {languages}\n🔖 Plot : {plot}\n\n♥️ Thanks for using me ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001552407504')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shorturllink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'bd7cbf1236df179f73bf7d2e2d8a45ea5f5fc04e')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/Tn68_tutorials/3"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/TN68_FilmFactory"

   # Auto Delete For Bot Sending Files #
