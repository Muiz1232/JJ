from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "27961050"))
    API_HASH = str(env.get("API_HASH", "9e5ca9e6da48a36c102ae9c8c8abac9f"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "7685546656:AAE3s1m8IUrxl1d6RUOPbPSSfUN0yNnXfIU"))
    OWNER_ID = int(env.get('OWNER_ID', '6334683599'))
    WORKERS = int(env.get("WORKERS", "10"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', "mongodb+srv://techsdev:Nm599r_CQHJ4it-@cluster0.x8pxe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "TELESERVICES_API"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', '-1002047763605')
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://api.teleservices.io/images/Teleservice_ed079bdeecba.jpg")
    START_PIC = env.get('START_PIC', "https://api.teleservices.io/images/Teleservice_ed079bdeecba.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://api.teleservices.io/images/Teleservice_ed079bdeecba.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", '-1002358747296'))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", '-1002358747296'))   # Logs channel for user logs
    MODE = env.get("MODE", "secondary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "5723455420")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



