# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# HANDLERS 1
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import add_user

from keyboard import main_menu



# ==========================================
# START COMMAND
# ==========================================


async def start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    user = update.effective_user


    add_user(user)



    await update.message.reply_text(

        f"""
🔥 <b>Вітаємо, {user.first_name}!</b>

🤖 UA ONLINE MEDIA BOT 4.0

Тут ти знайдеш:

📰 Новини
🎉 Івенти
🚀 Оновлення
🛠 Підтримку
💡 Пропозиції

Обери потрібний розділ нижче 👇
        """,

        parse_mode="HTML",

        reply_markup=main_menu()

    )



# ==========================================
# HELP COMMAND
# ==========================================


async def help_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    await update.message.reply_text(

        """
ℹ️ <b>Допомога UA ONLINE MEDIA BOT</b>


Команди:

/start — запуск бота

/news — новини

/events — івенти

/updates — оновлення

/support — техпідтримка


Якщо знайшли помилку — використовуйте:
/bug

        """,

        parse_mode="HTML"

    )



print("🚀 Handlers1 loaded")
