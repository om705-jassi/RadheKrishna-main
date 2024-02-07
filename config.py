import os

API_ID = API_ID =  6960732076

API_HASH = os.environ.get("API_HASH", "d7abcec5c967414fadb1d438fa05ebea")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6960732076:AAHuNQn7fB7RGfEW-BZM8t6SB8AaJGzFqBQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER",1403488629))

LOG = -1001998453704 

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1403488629 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


