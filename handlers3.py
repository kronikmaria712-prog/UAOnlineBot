# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# HANDLERS 3
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import (
    get_user,
    users_count
)



# ==========================================
# PROFILE
# ==========================================


async def profile(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    data = get_user(
        user.id
    )


    await update.message.reply_text(

        f"""
👤 <b>Ваш профіль</b>


🆔 ID: {user.id}

👤 Ім'я: {user.first_name}

📱 Username: @{user.username}


📅 Дата реєстрації:
{data[6] if data else "Немає даних"}

        """,

        parse_mode="HTML"

    )



# ==========================================
# STATISTICS
# ==========================================


async def stats(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    count = users_count()



    await update.message.reply_text(

        f"""
📊 <b>Статистика бота</b>


👥 Користувачів:
{count}


🤖 Версія:
4.0 Ultimate

        """,

        parse_mode="HTML"

    )



# ==========================================
# ABOUT BOT
# ==========================================


async def about(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    await update.message.reply_text(

        """
🤖 <b>UA ONLINE MEDIA BOT 4.0 ULTIMATE</b>


🔥 Можливості:

📰 Новини
🎉 Івенти
🚀 Оновлення
🛠 Підтримка
💡 Пропозиції
🐞 Баг-репорти
👑 Адмін система


Версія: 4.0

        """,

        parse_mode="HTML"

    )



print("👤 Handlers3 loaded")