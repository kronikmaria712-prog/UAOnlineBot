import sqlite3

# Підключення до бази даних
db = sqlite3.connect("ua_media.db", check_same_thread=False)
cursor = db.cursor()

# Користувачі
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    username TEXT,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Новини
cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    text TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Оновлення
cursor.execute("""
CREATE TABLE IF NOT EXISTS updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Івенти
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

db.commit()


def add_user(user):
    cursor.execute(
        "SELECT user_id FROM users WHERE user_id=?",
        (user.id,)
    )

    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO users(user_id, first_name, username) VALUES(?,?,?)",
            (
                user.id,
                user.first_name,
                user.username
            )
        )
        db.commit()


def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]