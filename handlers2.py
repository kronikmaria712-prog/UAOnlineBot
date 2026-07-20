# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# HANDLERS 2
# ==========================================


from telegram import Update
from telegram.ext import ContextTypes


from keyboard import main_menu, back_menu



# ==========================================
# MENU BUTTONS
# ==========================================


async def menu_buttons(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    query = update.callback_query

    await query.answer()


    data = query.data



    if data == "menu":


        await query.edit_message_text(

            """
🏠 <b>Головне меню</b>

Оберіть розділ:
            """,

            parse_mode="HTML",

            reply_markup=main_menu()

        )



    elif data == "news":


        await query.edit_message_text(

            "📰 Розділ новин відкрито.\n\nВикористайте /news",

            reply_markup=back_menu()

        )



    elif data == "updates":


        await query.edit_message_text(

            "🚀 Розділ оновлень.\n\nВикористайте /updates",

            reply_markup=back_menu()

        )



    elif data == "events":


        await query.edit_message_text(

            "🎉 Розділ івентів.\n\nВикористайте /events",

            reply_markup=back_menu()

        )



    elif data == "support":


        await query.edit_message_text(

            "🛠 Для звернення використайте /support",

            reply_markup=back_menu()

        )



print("🎛 Handlers2 loaded")
