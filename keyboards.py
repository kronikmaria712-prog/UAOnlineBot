from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("📰 Новини", callback_data="news"),
            InlineKeyboardButton("🚀 Оновлення", callback_data="updates"),
        ],
        [
            InlineKeyboardButton("🎉 Івенти", callback_data="events"),
            InlineKeyboardButton("👤 Профіль", callback_data="profile"),
        ],
        [
            InlineKeyboardButton("📊 Статистика", callback_data="stats"),
            InlineKeyboardButton("ℹ️ Про бота", callback_data="about"),
        ],
        [
            InlineKeyboardButton("📢 Канал", url="https://t.me/ВАШ_КАНАЛ")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def back_menu():
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu")]
    ]

    return InlineKeyboardMarkup(keyboard)


def admin_menu():
    keyboard = [
        [InlineKeyboardButton("📢 Розсилка", callback_data="broadcast")],
        [InlineKeyboardButton("📰 Додати новину", callback_data="add_news")],
        [InlineKeyboardButton("🚀 Додати оновлення", callback_data="add_update")],
        [InlineKeyboardButton("🎉 Додати івент", callback_data="add_event")],
        [InlineKeyboardButton("📊 Статистика", callback_data="admin_stats")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="menu")]
    ]

    return InlineKeyboardMarkup(keyboard)