##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'BQCsvGpRC8w6Y3K1BMbag71Ipo9XiR2t3ZfgjIXN7gmaIAC-PxC_hr79dE7pmCIb6t59WDVPYIrAeqz38M3Vepmk03tRUHz_-AQKUax_O-h4kjnQ278uE-m2lUG6pqQTzuuKc7_qfWNbM6HXlKYuflbRgtW5KPsDjG_dt3a5Y3L1i15QDVuBswhDCEXeepx4Y_2CzqrQV_PS0AWjOJ4CE-F1XHZFsOg3FjJOCYNZduRx0QwWHEzWuVzhTr_4n0uT_tx2BDH8yCEf7YuJxQ34wpC3bKnhELXF5ctRm-B6fLxY51y7Bh9jTwCNEASu3WPbgzubO1Qx_rNIQXPMbcSM7KAAAAAS4Lh4EA')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "11446036"))
API_HASH = getenv('API_HASH', "9fb20b211047e876fa3812ed18af2d4b")))
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '40000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001765271517'))
ASS_ID = int(getenv("ASS_ID", '5067474817'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/justteen/buzzmusiktelegram")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
