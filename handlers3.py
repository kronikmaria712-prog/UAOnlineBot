from telegram import Update
from telegram.ext import ContextTypes

from database import users_count
from keyboards import back_menu


# ==========================
# PROFILE
# ==========================

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user = query.from_user

    await query.edit_message_text(
        f"""
👤 <b>Профіль користувача</b>

🆔 ID: <code>{user.id}</code>
👤 Ім'я: {user.first_name}
📛 Username: @{user.username if user.username else "немає"}

💙 Дякуємо, що користуєтесь ботом!
""",
        parse_mode="HTML",
        reply_markup=back_menu()
    )


# ==========================
# STATS
# ==========================

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    count = users_count()

    await query.edit_message_text(
        f"""
📊 <b>Статистика</b>

👥 Користувачів бота: {count}

🤖 Версія: 3.0
""",
        parse_mode="HTML",
        reply_markup=back_menu()
    )


# ==========================
# ABOUT
# ==========================

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        """
ℹ️ <b>Про бота</b>

🤖 UA ONLINE MEDIA BOT

Версія: 3.0

Функції:
• Новини
• Оновлення
• Івенти
• Профіль
• Статистика

🚀 Бот постійно розвивається.
""",
        parse_mode="HTML",
        reply_markup=back_menu()
    )