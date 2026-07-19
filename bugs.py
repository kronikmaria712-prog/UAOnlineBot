# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# BUG REPORT SYSTEM
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import (
    add_bug,
    get_bugs,
    close_bug,
    is_admin
)



# ==========================================
# SEND BUG
# ==========================================


async def bug(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not context.args:

        await update.message.reply_text(
            "🐞 Напишіть опис бага:\n/bug текст"
        )

        return


    text = " ".join(context.args)


    add_bug(
        update.effective_user.id,
        text
    )


    await update.message.reply_text(
        """
✅ Баг відправлено!

Дякуємо за допомогу у покращенні бота.
        """
    )



# ==========================================
# ADMIN BUG LIST
# ==========================================


async def buglist(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(update.effective_user.id):

        await update.message.reply_text(
            "❌ Немає доступу."
        )

        return


    bugs = get_bugs()


    if not bugs:

        await update.message.reply_text(
            "🐞 Багів немає."
        )

        return


    text = "🐞 <b>Список багів:</b>\n\n"


    for item in bugs[:10]:

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
# CLOSE BUG (ADMIN)
# ==========================================


async def closebug(
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
            "❌ Приклад:\n/closebug ID"
        )

        return


    bug_id = int(context.args[0])


    close_bug(bug_id)


    await update.message.reply_text(
        "✅ Баг закрито."
    )



# ==========================================
# READY
# ==========================================

print("🐞 Bugs module loaded")
