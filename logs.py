# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# LOGS SYSTEM
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import (
    add_log,
    get_logs,
    is_admin
)



# ==========================================
# ADD LOG
# ==========================================


def create_log(
        user_id,
        action
):

    add_log(
        user_id,
        action
    )



# ==========================================
# SHOW LOGS (ADMIN)
# ==========================================


async def logs(
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



    data = get_logs()


    if not data:

        await update.message.reply_text(
            "📝 Логів поки немає."
        )

        return



    text = (
        "📝 <b>Останні дії:</b>\n\n"
    )


    for log in data[:20]:

        text += (
            f"👤 ID: {log[1]}\n"
            f"⚙️ {log[2]}\n"
            f"📅 {log[3]}\n\n"
        )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )



# ==========================================
# READY
# ==========================================

print("📝 Logs module loaded")

