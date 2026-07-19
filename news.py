# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# news.py
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes

from database import (
    add_news,
    get_news,
    delete_news
)


# ==========================================
# ADD NEWS
# ==========================================


async def addnews(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(
            "❌ Використання:\n/addnews Текст новини"
        )

        return


    text = " ".join(context.args)


    add_news(
        title="UA ONLINE NEWS",
        text=text,
        author=update.effective_user.id
    )


    await update.message.reply_text(
        """
✅ Новину додано!

📰 Вона збережена в базі.
        """
    )



# ==========================================
# SHOW NEWS
# ==========================================


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    news_list = get_news()


    if not news_list:

        await update.message.reply_text(
            "📰 Новин поки немає."
        )

        return


    text = "📰 <b>Останні новини:</b>\n\n"


    for item in news_list[:10]:

        text += (
            f"🔹 <b>{item[1]}</b>\n"
            f"{item[2]}\n"
            f"📅 {item[6]}\n\n"
        )


    await update.message.reply_text(
        text,
        parse_mode="HTML"
    )
    
    # ==========================================
# NEWS WITH PHOTO
# ==========================================


async def news_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message.photo:

        return


    photo = update.message.photo[-1].file_id


    caption = update.message.caption or "Без опису"


    add_news(
        title="UA ONLINE NEWS",
        text=caption,
        photo=photo,
        author=update.effective_user.id
    )


    await update.message.reply_text(
        "📸 Новину з фото збережено!"
    )



# ==========================================
# NEWS WITH VIDEO
# ==========================================


async def news_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message.video:

        return


    video = update.message.video.file_id


    caption = update.message.caption or "Без опису"


    add_news(
        title="UA ONLINE NEWS",
        text=caption,
        video=video,
        author=update.effective_user.id
    )


    await update.message.reply_text(
        "🎥 Новину з відео збережено!"
    )



# ==========================================
# DELETE NEWS
# ==========================================


async def remove_news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(
            "❌ Використання:\n/delnews ID"
        )

        return


    news_id = int(context.args[0])


    delete_news(news_id)


    await update.message.reply_text(
        "🗑 Новину видалено."
    )
    
    # ==========================================
# AUTO POST TO CHANNEL
# ==========================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import CHANNEL_ID, CHANNEL_LINK



async def publish_to_channel(
        context,
        title,
        text,
        photo=None,
        video=None
):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Наш Telegram канал",
                    url=CHANNEL_LINK
                )
            ]
        ]
    )


    message = (
        f"📰 <b>{title}</b>\n\n"
        f"{text}"
    )


    if photo:

        await context.bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo,
            caption=message,
            parse_mode="HTML",
            reply_markup=keyboard
        )


    elif video:

        await context.bot.send_video(
            chat_id=CHANNEL_ID,
            video=video,
            caption=message,
            parse_mode="HTML",
            reply_markup=keyboard
        )


    else:

        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode="HTML",
            reply_markup=keyboard
        )



# ==========================================
# NEWS READY
# ==========================================

print("📰 News module loaded")