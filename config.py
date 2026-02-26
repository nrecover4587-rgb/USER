import os

def env(key, default=None):
    return os.getenv(key, default)

API_ID = int(env("API_ID", "28483345"))
API_HASH = env("API_HASH", "0b04eb0deb137eb4d75bda5ca0bc49e8")

MONGO_URL = env(
    "MONGO_URL",
    "mongodb+srv://anmol:gII62eQDVpFw1SlZ@cluster0.k30u3uc.mongodb.net/?appName=Cluster0"
)

BOT_TOKEN = env("BOT_TOKEN", "8740569127:AAGePXwfx_vWMorJtk9dF2-ksz4CRbiD7Ac")

OWNER_ID = 7113972959
OWNER_USERNAME = "Mrmental001"   # <-- apna username bina @ ke likho

STRING_SESSION = env(
    "STRING_SESSION",
    "your_string_session_here"
)
