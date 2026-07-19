# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# support.py
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes

from database import (
    create_support,
    get_support,
    close_support
)


# ==========================================
# START SUPPORT
# ==========================================


async def support_start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        """
🛠 <b>Технічна підтримка UA ONLINE MEDIA</b>

Напишіть вашу проблему одним повідомленням.

Ми обов'язково розглянемо звернення.
        """,
        parse_mode="HTML"
    )

    context.user_data["support"] = True



# ==========================================
# SUPPORT MESSAGE
# ==========================================


async def support_message(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not context.user_data.get("support"):
        return


    message = update.message.text


    create_support(
        update.effective_user.id,
        message
    )


    context.user_data["support"] = False


    await update.message.reply_text(
        """
✅ Ваше звернення відправлено.

Очікуйте відповіді адміністрації.
        """
    )
    
    # ==========================================
# ADMIN SUPPORT LIST
# ==========================================


from database import is_admin



async def support_list(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(update.effective_user.id):

        await update.message.reply_text(
            "❌ Немає доступу."
        )

        return


    tickets = get_support()


    if not tickets:

        await update.message.reply_text(
            "📭 Заявок немає."
        )

        return


    text = "🛠 <b>Заявки підтримки:</b>\n\n"


    for ticket in tickets[:10]:

        text += (
            f"🆔 {ticket[0]}\n"
            f"👤 {ticket[1]}\n"
            f"💬 {ticket[2]}\n"
            f"📌 {ticket[3]}\n\n"
        )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )



# ==========================================
# CLOSE TICKET
# ==========================================


async def close_ticket(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(update.effective_user.id):

        return


    if not context.args:

        await update.message.reply_text(
            "Використання:\n/closeticket ID"
        )

        return


    ticket_id = int(context.args[0])


    close_support(ticket_id)


    await update.message.reply_text(
        "✅ Заявку закрито."
    )


# ==========================================
# SUPPORT READY
# ==========================================

print("🛠 Support module loaded")