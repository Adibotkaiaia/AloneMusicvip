#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/TheAloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/TheAloneMusic/blob/master/LICENSE >
# All rights reserved.
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# -------------------- TELEGRAM BASIC --------------------

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# -------------------- DATABASE --------------------

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# -------------------- OWNER --------------------

OWNER_ID = int(getenv("OWNER_ID", 8106551502))

# ❗ ADD THIS (VERY IMPORTANT FOR START BUTTON)
OWNER_USERNAME = getenv("OWNER_USERNAME", "YourUsername")  # without @

# -------------------- LIMITS --------------------

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# -------------------- LOGGING --------------------

LOGGER_ID = int(getenv("LOGGER_ID", 0))
DEBUG_IGNORE_LOG = True

# -------------------- HEROKU --------------------

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TheAloneTeam/AloneMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# -------------------- SUPPORT --------------------

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/Il_vip_support_lI"
)
SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/VIP_SUPPORT_II"
)

# -------------------- ASSISTANT --------------------

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# -------------------- SPOTIFY --------------------

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# -------------------- PLAYLIST --------------------

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# -------------------- FILE SIZE --------------------

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# -------------------- PYROGRAM STRING --------------------

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# -------------------- RUNTIME DATA --------------------

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# -------------------- IMAGES --------------------

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/gl1zbc.jpg",
)
PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/sgykuy.jpg",
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/hohfrh.jpg"
STATS_IMG_URL = "https://files.catbox.moe/gl1zbc.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/34xlvu.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/34xlvu.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"

# -------------------- TIME UTILS --------------------

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -------------------- URL CHECK --------------------

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )
