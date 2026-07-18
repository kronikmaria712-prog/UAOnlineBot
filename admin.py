from telegram import Update
from telegram.ext import ContextTypes

from database import users_count


# ==========================
# НАЛАШТУВАННЯ АДМІНА
# ==========================

ADMIN_ID = 8214220798 # ВСТАВ СВІЙ TELEGRAM ID


# ==========================
# ПЕРЕВІРКА АДМІНА
# ==========================

def is_admin(user_id):
    return user_id == ADMIN_ID


# ==========================
# АДМІН ПАНЕЛЬ
# ==========================

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    if not is_admin(user.id):
        await update.message.reply_text(
            "❌ У вас немає доступу!"
        )
        return

    await update.message.reply_text(
        """
👑 <b>Адмін-панель</b>

Доступні функції:

📊 /adminstats — статистика
📢 /broadcast — розсилка
📰 /addnews — додати новину

""",
        parse_mode="HTML"
    )


# ==========================
# СТАТИСТИКА
# ==========================

async def adminstats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not is_admin(update.effective_user.id):
        return

    count = users_count()

    await update.message.reply_text(
        f"""
📊 <b>Статистика</b>

👥 Користувачів: {count}
""",
        parse_mode="HTML"
    )


# ==========================
# РОЗСИЛКА
# ==========================

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not is_admin(update.effective_user.id):
        await update.message.reply_text(
            "❌ У вас немає доступу!"
        )
        return


    if not context.args:
        await update.message.reply_text(
            """
❌ Напиши текст для розсилки.

Приклад:
<code>/broadcast Привіт всім!</code>
""",
            parse_mode="HTML"
        )
        return


    text = " ".join(context.args)


    await update.message.reply_text(
        f"""
📢 <b>Розсилка створена!</b>

Текст:
{text}
""",
        parse_mode="HTML"
    )