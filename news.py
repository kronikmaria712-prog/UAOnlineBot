from telegram import Update
from telegram.ext import ContextTypes

from admin import is_admin


# ==========================
# СПИСОК НОВИН
# ==========================

news_list = []


# ==========================
# ДОДАТИ НОВИНУ
# ==========================

async def addnews(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not is_admin(update.effective_user.id):
        await update.message.reply_text(
            "❌ Немає доступу!"
        )
        return


    if not context.args:
        await update.message.reply_text(
            """
❌ Напиши текст новини.

Приклад:

/addnews Вийшло нове оновлення!
"""
        )
        return


    text = " ".join(context.args)

    news_list.append(text)


    await update.message.reply_text(
        f"""
📰 <b>Новину додано!</b>

{text}
""",
        parse_mode="HTML"
    )


# ==========================
# ПОКАЗАТИ НОВИНИ
# ==========================

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not news_list:
        await update.message.reply_text(
            "📰 Новин поки немає."
        )
        return


    text = "📰 <b>Останні новини:</b>\n\n"


    for i, item in enumerate(news_list, start=1):
        text += f"{i}. {item}\n\n"


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )