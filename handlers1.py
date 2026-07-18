from telegram import Update
from telegram.ext import ContextTypes

from database import add_user
from keyboards import main_menu


# ==========================
# START
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(user)

    await update.message.reply_text(
        f"""
🎮 <b>UA ONLINE MEDIA BOT</b>

👋 Вітаємо, {user.first_name}!

🔥 Інформаційний бот спільноти.

━━━━━━━━━━━━━━
📰 Новини
🚀 Оновлення
🎉 Івенти
👤 Профіль
📊 Статистика
━━━━━━━━━━━━━━

Оберіть розділ нижче 👇
""",
        parse_mode="HTML",
        reply_markup=main_menu()
    )


# ==========================
# HELP
# ==========================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
❓ <b>Допомога</b>

Команди:

/start — головне меню
/help — допомога

🤖 UA ONLINE MEDIA BOT
""",
        parse_mode="HTML"
    )