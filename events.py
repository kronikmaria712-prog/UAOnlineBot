# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# EVENTS SYSTEM
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from database import (
    is_admin,
    add_event,
    get_events,
    delete_event
)


# ==========================================
# SHOW EVENTS
# ==========================================


async def events(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    event_list = get_events()


    if not event_list:

        await update.message.reply_text(
            "🎉 Активних івентів зараз немає."
        )

        return


    text = "🎉 <b>Активні івенти UA ONLINE:</b>\n\n"


    for event in event_list:

        text += (
            f"🆔 ID: {event[0]}\n"
            f"⭐ {event[1]}\n"
            f"📝 {event[2]}\n"
            f"📅 {event[3]}\n\n"
        )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )



# ==========================================
# ADD EVENT (ADMIN)
# ==========================================


async def addevent(
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
            "❌ Приклад:\n/addevent Назва івенту"
        )

        return


    text = " ".join(context.args)


    add_event(
        title="UA ONLINE EVENT",
        text=text
    )


    await update.message.reply_text(
        "✅ Івент успішно створено!"
    )



# ==========================================
# DELETE EVENT (ADMIN)
# ==========================================


async def delevent(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not is_admin(update.effective_user.id):

        return


    if not context.args:

        await update.message.reply_text(
            "❌ Приклад:\n/delevent ID"
        )

        return


    event_id = int(context.args[0])


    delete_event(event_id)


    await update.message.reply_text(
        "🗑 Івент видалено."
    )



# ==========================================
# READY
# ==========================================

print("🎉 Events module loaded")
