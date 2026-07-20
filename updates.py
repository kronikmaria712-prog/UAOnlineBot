# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# UPDATES SYSTEM
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import (
    add_update,
    get_updates,
    is_admin,
    delete_update
)


# ==========================================
# SHOW UPDATES
# ==========================================


async def updates(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    update_list = get_updates()


    if not update_list:

        await update.message.reply_text(
            "🚀 Оновлень поки немає."
        )

        return


    text = "🚀 <b>Останні оновлення UA ONLINE:</b>\n\n"


    for item in update_list[:10]:

        text += (
            f"🆔 ID: {item[0]}\n"
            f"⭐ {item[1]}\n"
            f"📝 {item[2]}\n"
            f"📅 {item[3]}\n\n"
        )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )



# ==========================================
# ADD UPDATE (ADMIN)
# ==========================================


async def addupdate(
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
            "❌ Приклад:\n/addupdate Назва оновлення"
        )

        return


    text = " ".join(context.args)


    add_update(
        title="UA ONLINE UPDATE",
        text=text
    )


    await update.message.reply_text(
        "✅ Оновлення додано!"
    )
    
    # ==========================================
# DELETE UPDATE (ADMIN)
# ==========================================


async def delupdate(
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
            "❌ Приклад:\n/delupdate ID"
        )

        return


    update_id = int(context.args[0])


    delete_update(update_id)


    await update.message.reply_text(
        "🗑 Оновлення видалено."
    )



# ==========================================
# READY
# ==========================================

print("🚀 Updates module loaded")
