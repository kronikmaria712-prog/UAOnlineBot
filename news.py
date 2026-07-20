# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# news.py
# ==========================================

from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from database import (
    add_news,
    get_news,
    delete_news
)

from config import CHANNEL_ID,CHANNEL_LINK


# ==========================================
# AUTO POST TO CHANNEL HELPER
# ==========================================

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

    try:
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
        return True
    except Exception as e:
        print(f"Помилка автопостингу: {e}")
        return False


# ==========================================
# ADD NEWS (TEXT OR PHOTO/VIDEO WITH CAPTION)
# ==========================================

async def addnews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    
    # Визначаємо чи є фото/відео та текст/підпис
    photo = message.photo[-1].file_id if message.photo else None
    video = message.video.file_id if message.video else None
    
    caption = message.caption or ""
    text_args = " ".join(context.args) if context.args else ""
    
    text = text_args if text_args else caption

    if not text and not photo and not video:
        await message.reply_text(
            "❌ Використання:\n/addnews Текст новини (або додай фото/відео з підписом та командою /addnews)"
        )
        return

    title = "UA ONLINE NEWS"
    author_id = message.from_user.id

    # 1. Зберігаємо новину в базу даних
    add_news(
        title=title,
        text=text,
        photo=photo,
        video=video,
        author=author_id
    )

    # 2. Автоматично публікуємо в Telegram-канал
    success = await publish_to_channel(
        context=context,
        title=title,
        text=text,
        photo=photo,
        video=video
    )

    channel_status = "\n📢 Та успішно опубліковано в канал!" if success else "\n⚠️ Помилка автопостингу в канал!"

    # 3. Звіт адміністратору
    await message.reply_text(
        f"✅ Новину успішно додано в базу!{channel_status}",
        parse_mode="HTML"
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
# NEWS READY
# ==========================================

print("📰 News module loaded")
