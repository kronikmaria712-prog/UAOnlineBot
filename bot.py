# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# bot.py
# ==========================================


from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)


# ==========================================
# CONFIG
# ==========================================

from config import TOKEN


# ==========================================
# HANDLERS
# ==========================================

from handlers1 import start, help_command
from handlers2 import menu_buttons
from handlers3 import profile, stats, about


# ==========================================
# MODULES
# ==========================================

from news import news, addnews
from admin import admin, adminstats, broadcast
from support import support_start, support_message
from events import events
from updates import updates

from bugs import bug, buglist, closebug

from suggestions import (
    suggestion,
    suggestion_list,
    closesuggestion
)

from backup import backup
from logs import logs



# ==========================================
# START
# ==========================================

async def start_bot(update, context):
    await start(update, context)



# ==========================================
# MAIN
# ==========================================

def main():

    app = Application.builder().token(TOKEN).build()


    # ==========================
    # USER COMMANDS
    # ==========================

    app.add_handler(
        CommandHandler(
            "start",
            start_bot
        )
    )

    app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )

    app.add_handler(
        CommandHandler(
            "news",
            news
        )
    )

    app.add_handler(
        CommandHandler(
            "events",
            events
        )
    )

    app.add_handler(
        CommandHandler(
            "updates",
            updates
        )
    )


    # ==========================
    # PROFILE
    # ==========================

    app.add_handler(
        CommandHandler(
            "profile",
            profile
        )
    )

    app.add_handler(
        CommandHandler(
            "stats",
            stats
        )
    )

    app.add_handler(
        CommandHandler(
            "about",
            about
        )
    )


    # ==========================
    # ADMIN
    # ==========================

    app.add_handler(
        CommandHandler(
            "admin",
            admin
        )
    )

    app.add_handler(
        CommandHandler(
            "adminstats",
            adminstats
        )
    )

    app.add_handler(
        CommandHandler(
            "broadcast",
            broadcast
        )
    )

    app.add_handler(
        CommandHandler(
            "addnews",
            addnews
        )
    )


    # ==========================
    # SUPPORT
    # ==========================

    app.add_handler(
        CommandHandler(
            "support",
            support_start
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            support_message
        )
    )


    # ==========================
    # BUGS
    # ==========================

    app.add_handler(
        CommandHandler(
            "bug",
            bug
        )
    )

    app.add_handler(
        CommandHandler(
            "buglist",
            buglist
        )
    )

    app.add_handler(
        CommandHandler(
            "closebug",
            closebug
        )
    )


    # ==========================
    # SUGGESTIONS
    # ==========================

    app.add_handler(
        CommandHandler(
            "suggestion",
            suggestion
        )
    )

    app.add_handler(
        CommandHandler(
            "suggestion_list",
            suggestion_list
        )
    )

    app.add_handler(
        CommandHandler(
            "closesuggestion",
            closesuggestion
        )
    )


    # ==========================
    # BACKUP + LOGS
    # ==========================

    app.add_handler(
        CommandHandler(
            "backup",
            backup
        )
    )

    app.add_handler(
        CommandHandler(
            "logs",
            logs
        )
    )


    # ==========================
    # BUTTONS
    # ==========================

    app.add_handler(
        CallbackQueryHandler(
            menu_buttons,
            pattern="^(menu|news|events|updates|support)$"
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
    # RUN
    # ==========================

    print("=" * 40)
    print("🤖 UA ONLINE MEDIA BOT 4.0 ULTIMATE")
    print("✅ Бот успішно запущений")
    print("=" * 40)


    app.run_polling()



# ==========================================
# START FILE
# ==========================================

if __name__ == "__main__":
    main()