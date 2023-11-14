#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler


USELESS_TEXT = os.environ.get("USELESS_TEXT", "1")
USELESS_TEXT2 = os.environ.get("USELESS_TEXT2", "1")
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6088268558:AAGfWYXYp-LCZVOFhy-weOSpwZtaO5AQoXA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16844842"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f6b0ceec5535804be7a56ac71d08a5d4")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001920102302"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5821581983"))

#Port
PORT = os.environ.get("PORT", "8287")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kacxx1:mongo123@cluster0.ownatea.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "LocusFileBot"")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6265459491 5821581983").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
        
try:
    CHANNEL_ADMINS=[]
    for x in (os.environ.get("CHANNEL_ADMINS", "5821581983 6265459491 5751548638").split()):
        CHANNEL_ADMINS.append(int(x))
except ValueError:
        raise Exception("Your channel Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5821581983)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
