import json
import os


def get_user_list(config, key):
    with open("{}/KRISTY/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
     
    API_ID = 15418866  # integer value, dont use "" this sign get it form my.telegram.org
    API_HASH = "dbbf679a4b429fab1bfea0b52b8f9be8" # get it form my.telegram.org
    TOKEN = "6091958748:AAEcw9e0jdy381xxQVeWUuV1eCoDSE7C3dA"  # get it form @botfather.
    OWNER_ID = 5897579715 # got to @miss_kristy_bot and type /id
    OWNER_USERNAME = "I_AM_PRO_KING" # your telegram username
    ALLOW_CHATS = True # leave it as it is
    BOT_USERNAME = "Harshop12_musicbot" # your bot username get it form @botfather
    SUPPORT_CHAT = "chatting_gruap"  # Your own group for support, do not add the @ if you dont have leave it as it is
    UPDATES_CHANNEL = "chatting_gruap"  # Your own chsnnel for support, do not add the @ if you dont have leave it as it is
    JOIN_LOGGER =  (
        -1001618068091
    )  # add @miss_kristy_bot in your group and type /id
    EVENT_LOGS = (
        -1001618068091
    )  # add @miss_kristy_bot in your group and type /id
    ERROR_LOG = (
        -1001618068091
    )  # add @miss_kristy_bot in your group and type /id
    STRICT_GMUTE = True #to allow gmutes
    START_STICKER = "CAACAgUAAxkBAAIGqWPbjJSS9VN78jnh6k8sL2Z3cgP3AALDBgACE9chVDfb3d0QhpUCLgQ" #sticker id for start animation
    TEMP_DOWNLOAD_DIRECTORY = ". /" # dont change
    OPENWEATHERMAP_ID = None



    # RECOMMENDED
    STRING_SESSION ="BQAoAyn21syI26TYs0_0H7NMU2P0kt0vZ7dxCCqv83z3NcDULz9ETFVax4Wl5hQMWlnezAY7JTrjGuXCM6blSy2xIWkEH3ISDY4x_sr7Ot_TCy2AY8fp3wyPnSKN_v3ZCPKTcJt4bdMoqsypqWove9aG4yAl4defkzFLYSkosZW3FJBYzQgeoYJkGQMR4IPiYXUwNHdwQv1XpuXUeJcMJGm9Z3PI5WQ6m0BJ8-YNMgqKK6P_QZxcbF_B4SzrvC0_0M4SBJQkvnNSwSe7r08dE5c8YaXiRyVvc95_lJ4FYLiMlApv5pfMT6UNnotTaWpJ1YVK4Z2UIKxW9QOD24IaaYpkAAAAAV-F7MMA" #telethon string session of user or bot get it from https://replit.com/@MISSKRISTY/MISS-KRISTY
    MONGO_DB_URI = "mongodb+srv://vcbot:vcbot@cluster0.yqipgxg.mongodb.net/?retryWrites=true&w=majority" #get it from mongodb.com get
    ARQ_API_KEY = "" #git it form @ARQRobot
    ARQ_API_URL = "https://arq.hamker.in" # dont change
    SQLALCHEMY_DATABASE_URL = "postgres://xcjxxdmr:WL1DeXGfom6CvKzMwsD6h5ZR_UKhTDlS@hattie.db.elephantsql.com/xcjxxdmr"  # needed for any database modules get it from https://www.elephantsql.com/
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "chatting_gruap"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@"


    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = [1820525265]
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [1820525265]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = [1820525265]
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = [1820525265]
    WOLVES = [1820525265]
    START_IMG = "https://te.legra.ph/file/963350097d10d22508deb.jpg" #yor fav img link
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    REM_BG_API_KEY = "uwu"
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = None  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
