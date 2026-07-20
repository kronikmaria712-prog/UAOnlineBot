# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# config.py
# ==========================================

# ==========================
# TELEGRAM
# ==========================

TOKEN = "8864985987:AAGEeuncaqJ2vPhs-J1yualELeSmu443pxg"

# Telegram канал (числовий ID каналу)
CHANNEL_ID = -1003891003399
CHANNEL_LINK = "https://t.me/uaonline_newsua"

# ==========================
# ВЛАСНИК
# ==========================

OWNER_ID = 8214220798

# ==========================
# АДМІНІСТРАТОРИ
# ==========================

ADMINS = [
    OWNER_ID,
]

# ==========================
# ПРОЄКТ
# ==========================

BOT_NAME = "UA ONLINE MEDIA BOT"

BOT_VERSION = "4.0 Ultimate"

# ==========================
# DATABASE
# ==========================

DATABASE_NAME = "database.db"

# ==========================
# BACKUP
# ==========================

BACKUP_ENABLED = True

# ==========================
# LOGS
# ==========================

LOGS_ENABLED = True

# ==========================
# MODULES
# ==========================

NEWS_ENABLED = True

SUPPORT_ENABLED = True

EVENTS_ENABLED = True

UPDATES_ENABLED = True

SUGGESTIONS_ENABLED = True

BUGS_ENABLED = True

BROADCAST_ENABLED = True

STATISTICS_ENABLED = True

# ==========================
# LIMITS
# ==========================

MAX_BROADCAST = 100000

MAX_NEWS_LENGTH = 4000

MAX_SUPPORT_LENGTH = 3000

# ==========================
# TIME
# ==========================

TIMEZONE = "Europe/Kyiv"

# ==========================
# MEDIA
# ==========================

ALLOW_PHOTO = True

ALLOW_VIDEO = True

ALLOW_DOCUMENTS = True

ALLOW_STICKERS = True

# ==========================
# SECURITY
# ==========================

ONLY_ADMINS_CAN_POST = True

ONLY_OWNER_CAN_DELETE_ADMINS = True
