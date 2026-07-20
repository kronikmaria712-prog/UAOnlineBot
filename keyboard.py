# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# KEYBOARD SYSTEM
# ==========================================

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

# ==========================================
# MAIN MENU
# ==========================================

def main_menu():

    keyboard = [

        [
            InlineKeyboardButton("📥 Скачати гру", url="https://www.ua-online.games"),
            InlineKeyboardButton("📢 ТГ Канал", url="https://t.me/uaonline_newsua")
        ],

        [
            InlineKeyboardButton("📰 Новини", callback_data="news"),
            InlineKeyboardButton("🚀 Оновлення", callback_data="updates")
        ],

        [
            InlineKeyboardButton("🎉 Івенти", callback_data="events"),
            InlineKeyboardButton("👤 Профіль", callback_data="profile")
        ],

        [
            InlineKeyboardButton("🛠 Підтримка", callback_data="support")
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )

# ==========================================
# CHANNEL BUTTON
# ==========================================

def channel_button():

    keyboard = [

        [
            InlineKeyboardButton(
                "📢 Наш Telegram канал",
                url="https://t.me/uaonline_newsua"
            )
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )

# ==========================================
# BACK BUTTON
# ==========================================

def back_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "⬅️ Назад",
                callback_data="menu"
            )
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )

print("🎛 Keyboard module loaded")
