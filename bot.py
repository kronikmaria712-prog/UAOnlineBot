from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler
)

# Основні обробники
from handlers1 import start, help_command
from handlers2 import menu_buttons
from handlers3 import profile, stats, about

# Новини
from news import addnews, news

# Адмінка
from admin import admin, adminstats, broadcast


# ==========================
# ТОКЕН БОТА
# ==========================

TOKEN = "8864985987:AAGEeuncaqJ2vPhs-J1yualELeSmu443pxg"


# ==========================
# ЗАПУСК
# ==========================

def main():

    app = Application.builder().token(TOKEN).build()


    # ==========================
    # КОМАНДИ КОРИСТУВАЧІВ
    # ==========================

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    # ==========================
    # НОВИНИ
    # ==========================

    app.add_handler(
        CommandHandler("addnews", addnews)
    )

    app.add_handler(
        CommandHandler("news", news)
    )


    # ==========================
    # КНОПКИ МЕНЮ
    # ==========================

    app.add_handler(
        CallbackQueryHandler(
            menu_buttons,
            pattern="^(news|updates|events|menu)$"
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            profile,
            pattern="^profile$"
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            stats,
            pattern="^stats$"
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            about,
            pattern="^about$"
        )
    )


    # ==========================
    # АДМІН КОМАНДИ
    # ==========================

    app.add_handler(
        CommandHandler("admin", admin)
    )

    app.add_handler(
        CommandHandler("adminstats", adminstats)
    )

    app.add_handler(
        CommandHandler("broadcast", broadcast)
    )


    print("==============================")
    print("🤖 UA ONLINE MEDIA BOT 3.0")
    print("✅ Бот успішно запущений")
    print("==============================")


    app.run_polling()


# ==========================
# START
# ==========================

if __name__ == "__main__":
    main()