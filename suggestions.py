# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# SUGGESTIONS SYSTEM
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import (
    add_suggestion,
    get_suggestions,
    close_suggestion,
    is_admin
)



# ==========================================
# SEND SUGGESTION
# ==========================================


async def suggestion(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not context.args:

        await update.message.reply_text(
            "💡 Напишіть вашу пропозицію:\n/suggestion текст"
        )

        return


    text = " ".join(context.args)


    add_suggestion(
        update.effective_user.id,
        text
    )


    await update.message.reply_text(
        """
✅ Пропозицію відправлено!

Дякуємо за ідею.
        """
    )



# ==========================================
# ADMIN SUGGESTIONS
# ==========================================


async def suggestion_list(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(update.effective_user.id):

        await update.message.reply_text(
            "❌ Немає доступу."
        )

        return


    suggestions = get_suggestions()


    if not suggestions:

        await update.message.reply_text(
            "💡 Пропозицій немає."
        )

        return


    text = "💡 <b>Пропозиції користувачів:</b>\n\n"


    for item in suggestions[:10]:

        text += (
            f"🆔 {item[0]}\n"
            f"👤 {item[1]}\n"
            f"💬 {item[2]}\n"
            f"📌 {item[3]}\n\n"
        )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )
    # ==========================================
# CLOSE SUGGESTION (ADMIN)
# ==========================================


async def closesuggestion(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(update.effective_user.id):

        await update.message.reply_text(
            "❌ Немає доступу."
        )

        return


    if not context.args:

        await update.message.reply_text(
            "❌ Приклад:\n/closesuggestion ID"
        )

        return


    suggestion_id = int(context.args[0])


    close_suggestion(
        suggestion_id
    )


    await update.message.reply_text(
        "✅ Пропозицію закрито."
    )



# ==========================================
# READY
# ==========================================

print("💡 Suggestions module loaded")
