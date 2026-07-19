# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# BACKUP SYSTEM
# ==========================================


import sqlite3
import shutil
from datetime import datetime


from telegram import Update
from telegram.ext import ContextTypes


from database import is_admin



# ==========================================
# CREATE BACKUP
# ==========================================


def create_backup():

    date = datetime.now().strftime(
        "%Y-%m-%d_%H-%M"
    )


    backup_name = (
        f"backup_database_{date}.db"
    )


    shutil.copy(
        "database.db",
        backup_name
    )


    return backup_name



# ==========================================
# ADMIN BACKUP COMMAND
# ==========================================


async def backup(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(
        update.effective_user.id
    ):

        await update.message.reply_text(
            "❌ Немає доступу."
        )

        return



    file = create_backup()


    await update.message.reply_text(
        f"""
✅ Резервну копію створено!

💾 Файл:
{file}
        """
    )



# ==========================================
# READY
# ==========================================

print("💾 Backup module loaded")

