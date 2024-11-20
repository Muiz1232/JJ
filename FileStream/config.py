from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", 26183755))
    API_HASH = str(env.get("API_HASH", "7b7cfa427476172beb5ef3815209b747"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "7685546656:AAE3s1m8IUrxl1d6RUOPbPSSfUN0yNnXfIU"))
    OWNER_ID = int(env.get('OWNER_ID', '6334683599'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', "mongodb+srv://soumyadeepdas765:YcmoyvHBlXKIkueO@cluster0.yemc5.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "TELESERVICES_API"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://api.teleservices.io/images/Teleservice_ed079bdeecba.jpg")
    START_PIC = env.get('START_PIC', "https://api.teleservices.io/images/Teleservice_ed079bdeecba.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://api.teleservices.io/images/Teleservice_ed079bdeecba.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002358747296"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002358747296"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "6334683599")).split()))

class Server:
    PORT = int(env.get("PORT", 80))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
