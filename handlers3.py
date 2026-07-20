# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# HANDLERS 3 (ВИПРАВЛЕНИЙ)
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes

from database import (
    get_user,
    users_count
)

from keyboard import back_menu


# ==========================================
# PROFILE
# ==========================================


async def profile(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    # Визначаємо, звідки прийшов запит: від кнопки чи від команди
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        user = query.from_user
        target_message = query.message
        is_callback = True
    else:
        user = update.effective_user
        target_message = update.message
        is_callback = False


    data = get_user(
        user.id
    )

    text = (
        f"👤 <b>Ваш профіль</b>\n\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"👤 Ім'я: {user.first_name}\n"
        f"📱 Username: @{user.username if user.username else 'не вказано'}\n\n"
        f"📅 Дата реєстрації:\n"
        f"{data[6] if data else 'Немає даних'}"
    )

    # Відправляємо залежно від того, як викликали
    if is_callback:
        await target_message.edit_text(
            text,
            parse_mode="HTML",
            reply_markup=back_menu()
        )
    else:
        await target_message.reply_text(
            text,
            parse_mode="HTML",
            reply_markup=back_menu()
        )



# ==========================================
# STATISTICS
# ==========================================


async def stats(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if update.callback_query:
        await update.callback_query.answer()
        target = update.callback_query.message
        is_callback = True
    else:
        target = update.message
        is_callback = False

    count = users_count()

    text = (
        f"📊 <b>Статистика бота</b>\n\n"
        f"👥 Користувачів:\n{count}\n\n"
        f"🤖 Версія:\n4.0 Ultimate"
    )

    if is_callback:
        await target.edit_text(text, parse_mode="HTML", reply_markup=back_menu())
    else:
        await target.reply_text(text, parse_mode="HTML", reply_markup=back_menu())



# ==========================================
# ABOUT BOT
# ==========================================


async def about(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if update.callback_query:
        await update.callback_query.answer()
        target = update.callback_query.message
        is_callback = True
    else:
        target = update.message
        is_callback = False

    text = (
        f"🤖 <b>UA ONLINE MEDIA BOT 4.0 ULTIMATE</b>\n\n"
        f"🔥 Можливості:\n\n"
        f"📰 Новини\n"
        f"🎉 Івенти\n"
        f"🚀 Оновлення\n"
        f"🛠 Підтримка\n"
        f"💡 Пропозиції\n"
        f"🐞 Баг-репорти\n"
        f"👑 Адмін система\n\n"
        f"Версія: 4.0"
    )

    if is_callback:
        await target.edit_text(text, parse_mode="HTML", reply_markup=back_menu())
    else:
        await target.reply_text(text, parse_mode="HTML", reply_markup=back_menu())



print("👤 Handlers3 loaded successfully")
