
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "17250424" # integer value, dont use ""
    API_HASH = "753bc98074d420ef57ddf7eb1513162b"
    TOKEN = "6884805679:AAEGquSzbfBkTLknKgJVZ_QtSmhVfj4A42g"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6024180996 # If you dont know, run the bot and do /id in your private chat with it, also an integer

    MUST_JOIN = "Berlinmusic_support"
    SUPPORT_CHAT = "Berlinmusic_support"  # Your own group for support, do not add the @
    START_IMG = "https://graph.org/file/b87a43a56db9f6e7e3835.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://babunt2:1234@cluster0.iyq8qsn.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = [6024180996]  # List of groups that you want blacklisted.
    DRAGONS = [6024180996]  # User id of sudo users
    DEV_USERS = [6024180996]  # User id of dev users
    DEMONS = [6024180996]  # User id of support users
    TIGERS = [6024180996]  # User id of tiger users
    WOLVES = [6024180996]  # User id of whitelist users

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
