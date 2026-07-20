# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# admin.py
# ==========================================

from telegram import Update
from telegram.ext import ContextTypes
from config import OWNER_ID

from database import (
    is_admin,
    users_count,
    get_statistics,
    get_users,
    add_admin,
    remove_admin,
    add_news,
    delete_news,
    get_news,
    add_log
)

# ==========================================
# SECRET ADMIN COMMAND (Швидкий доступ за ID)
# ==========================================

async def secret_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text("❌ Введіть пароль.")
        return

    password = context.args[0]

    try:
        if int(password) == OWNER_ID and user_id == OWNER_ID:
            context.user_data["is_admin"] = True
            await update.message.reply_text(
                "👑 <b>Вітаю, шефе!</b> Секретний доступ активовано.\n\n"
                "📊 /adminstats\n"
                "📢 /broadcast\n"
                "📰 /addnews",
                parse_mode="HTML"
            )
        else:
            await update.message.reply_text("❌ Неправильний пароль або немає доступу.")
    except ValueError:
        await update.message.reply_text("❌ Пароль має складатися з цифр.")

# ==========================================
# ADMIN PANEL
# ==========================================

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Дозволяємо доступ або якщо пройшов секретну перевірку, або через базу/конфіг
    if not is_admin(user_id) and not context.user_data.get("is_admin"):
        await update.message.reply_text("❌ У вас немає доступу до адмін-панелі.")
        return

    await update.message.reply_text(
        """
👑 <b>UA ONLINE MEDIA BOT 4.0</b>

🛠 Адмін-панель

Доступні команди:

📊 /adminstats
📢 /broadcast
📰 /addnews
        """,
        parse_mode="HTML"
    )

# ==========================================
# ADMIN STATISTICS
# ==========================================

async def adminstats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_admin(user_id) and not context.user_data.get("is_admin"):
        await update.message.reply_text("❌ Немає доступу.")
        return

    stats = get_statistics()

    await update.message.reply_text(
        f"""
📊 <b>Статистика бота</b>

👥 Користувачі: {stats['users']}
📰 Новини: {stats['news']}
🎉 Івенти: {stats['events']}
🚀 Оновлення: {stats['updates']}
        """,
        parse_mode="HTML"
    )

# ==========================================
# BROADCAST
# ==========================================

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_admin(user_id) and not context.user_data.get("is_admin"):
        await update.message.reply_text("❌ Немає доступу.")
        return

    if not context.args:
        await update.message.reply_text("❌ Використання:\n/broadcast Текст повідомлення")
        return

    text = " ".join(context.args)
    users = get_users()
    sent = 0

    for user in users:
        try:
            await context.bot.send_message(chat_id=user[1], text=text)
            sent += 1
        except Exception:
            pass

    await update.message.reply_text(f"✅ Розсилка завершена\n\n📨 Відправлено: {sent}")

# ==========================================
# ADD ADMIN
# ==========================================

async def addadmin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id) and not context.user_data.get("is_admin"):
        return

    if not context.args:
        await update.message.reply_text("Використання:\n/addadmin ID Ранг")
        return

    user_id = int(context.args[0])
    rank = " ".join(context.args[1:]) or "Admin"

    add_admin(user_id, rank)
    await update.message.reply_text("✅ Адміністратора додано.")

# ==========================================
# REMOVE ADMIN
# ==========================================

async def deladmin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id) and not context.user_data.get("is_admin"):
        return

    if not context.args:
        await update.message.reply_text("Використання:\n/deladmin ID")
        return

    user_id = int(context.args[0])
    remove_admin(user_id)
    await update.message.reply_text("✅ Адміністратора видалено.")

# ==========================================
# NEWS MANAGEMENT
# ==========================================

async def addnews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id) and not context.user_data.get("is_admin"):
        await update.message.reply_text("❌ Немає доступу.")
        return

    if not context.args:
        await update.message.reply_text("❌ Використання:\n/addnews Заголовок | Текст")
        return

    full_text = " ".join(context.args)

    if "|" in full_text:
        title, news_text = full_text.split("|", 1)
        
        add_news(
            title=title.strip(),
            text=news_text.strip(),
            author=update.effective_user.id
        )
        
        add_log(
            update.effective_user.id,
            "Додав новину"
        )
        
        await update.message.reply_text("✅ Новину успішно додано!")
    else:
        await update.message.reply_text("❌ Помилка! Використовуйте формат: /addnews Заголовок | Текст")
