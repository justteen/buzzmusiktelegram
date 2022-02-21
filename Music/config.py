##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "1457097205"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '40000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001765271517'))
ASS_ID = int(getenv("ASS_ID", '5067474817'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/justteen/buzzmusiktelegram")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
