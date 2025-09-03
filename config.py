# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "26994377"))
API_HASH = getenv("API_HASH", "9c9eb74a4a0a1ecd4c96abebf3c637ee")
BOT_TOKEN = getenv("BOT_TOKEN", "7509054778:AAEcs-eHWpie4SWDgxF38yFFL28UVthUeA4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8184789731").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fixmayart834:FMWwXBd4JJYMs2Iv@cluster0.ltpube9.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1003087587927")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003024428633"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
