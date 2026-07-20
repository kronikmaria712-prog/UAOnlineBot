# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# sub_check.py (ПЕРЕВІРКА ПІДПИСКИ)
# ==========================================

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import CHANNEL_ID, CHANNEL_LINK, OWNER_ID

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user_id = update.effective_user.id
    
    # Власника бота пропускаємо завжди
    if user_id == OWNER_ID:
        return True

    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Помилка перевірки підписки: {e}")
        return True

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Підписатися на канал", url=CHANNEL_LINK)],
    ])

    text = (
        "⚠️ <b>Упс! Ви не підписані на наш Telegram-канал!</b>\n\n"
        "Щоб користуватися цією функцією, будь ласка, підпишіться на офіційний канал проєкту, а потім повторіть спробу. 👇"
    )

    if update.message:
        await update.message.reply_text(text, parse_mode="HTML", reply_markup=keyboard)
    elif update.callback_query:
        await update.callback_query.answer("Ви не підписані на канал! ❌", show_alert=True)

    return False
