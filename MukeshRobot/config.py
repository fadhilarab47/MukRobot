
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "16452568" # integer value, dont use ""
    API_HASH = "f936697c5c9e5bffd433babef7a4e4c9"
    TOKEN = "6515197149:AAEUZdUatsvt_t1ElCqWB2qDl5wEg6Ca9DM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1948147616 # If you dont know, run the bot and do /id in your private chat with it, also an integer

    MUST_JOIN = "SiArab_Support"
    SUPPORT_CHAT = "SiArab_Support"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph//file/3900ea5b3385ac7632dac.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://doadmin:9r260Iqy437zS1lA@db-mongodb-sgp1-52558-1312a8db.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-52558"
    # RECOMMENDED
    DATABASE_URL = "postgresql://doadmin:AVNS_AbvumOGAgERUr-xVj-n@db-postgresql-sgp1-66543-do-user-15262677-0.c.db.ondigitalocean.com:25060/defaultdb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "J1BBEIOV38CZ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "ZMOE8Q6BE25J7BEU"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1948147616]  # User id of sudo users
    DEV_USERS = [1948147616]  # User id of dev users
    DEMONS = [1948147616]  # User id of support users
    TIGERS = [1948147616]  # User id of tiger users
    WOLVES = [1948147616]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
