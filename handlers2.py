from telegram import Update
from telegram.ext import ContextTypes

from keyboards import back_menu


# ==========================
# BUTTONS - NEWS / UPDATES / EVENTS
# ==========================

async def menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()


    # 📰 Новини
    if query.data == "news":

        await query.edit_message_text(
            """
📰 <b>Новини</b>

Поки що новин немає.

Слідкуйте за оновленнями!
""",
            parse_mode="HTML",
            reply_markup=back_menu()
        )


    # 🚀 Оновлення
    elif query.data == "updates":

        await query.edit_message_text(
            """
🚀 <b>Оновлення</b>

Нових оновлень поки немає.

Ми працюємо над покращенням бота!
""",
            parse_mode="HTML",
            reply_markup=back_menu()
        )


    # 🎉 Івенти
    elif query.data == "events":

        await query.edit_message_text(
            """
🎉 <b>Івенти</b>

Активних івентів немає.

Нові події з'являться тут!
""",
            parse_mode="HTML",
            reply_markup=back_menu()
        )


    # ⬅️ Назад
    elif query.data == "menu":

        from keyboards import main_menu

        await query.edit_message_text(
            "🏠 Головне меню:",
            reply_markup=main_menu()
        )		