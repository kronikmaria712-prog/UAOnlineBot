import sqlite3
from config import ADMINS

db = sqlite3.connect("database.db", check_same_thread=False)
cursor = db.cursor()

# Таблиці
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, first_name TEXT, last_name TEXT, username TEXT, language TEXT, join_date TEXT, last_activity TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS admins(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, rank TEXT, date_add TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS news(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT, photo TEXT, video TEXT, author INTEGER, date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS support(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, message TEXT, status TEXT, date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS bugs(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, message TEXT, status TEXT, date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS suggestions(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, message TEXT, status TEXT, date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, action TEXT, date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT, date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS updates(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT, date TEXT)")

# --- USER ---
def add_user(user):
    cursor.execute("INSERT OR IGNORE INTO users(user_id, first_name, last_name, username, language, join_date) VALUES(?,?,?,?,?,datetime('now'))", (user.id, user.first_name or "", user.last_name or "", user.username or "", user.language_code or ""))
    db.commit()

def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

# --- ADMIN & LOGS ---
def is_admin(user_id):
    if user_id in ADMINS: return True
    cursor.execute("SELECT * FROM admins WHERE user_id=?", (user_id,))
    return cursor.fetchone() is not None

def add_admin(user_id, rank="admin"):
    cursor.execute("INSERT OR IGNORE INTO admins(user_id, rank, date_add) VALUES(?,?,datetime('now'))", (user_id, rank))
    db.commit()

def remove_admin(user_id):
    cursor.execute("DELETE FROM admins WHERE user_id=?", (user_id,))
    db.commit()

def add_log(user_id, action):
    cursor.execute("INSERT INTO logs(user_id, action, date) VALUES(?,?,datetime('now'))", (user_id, action))
    db.commit()

def get_logs():
    cursor.execute("SELECT * FROM logs ORDER BY id DESC")
    return cursor.fetchall()

# --- EVENTS & UPDATES ---
def add_event(title, text, date):
    cursor.execute("INSERT INTO events(title, text, date) VALUES(?,?,?)", (title, text, date))
    db.commit()

def get_events():
    cursor.execute("SELECT * FROM events ORDER BY id DESC")
    return cursor.fetchall()

def delete_event(event_id):
    cursor.execute("DELETE FROM events WHERE id=?", (event_id,))
    db.commit()

def add_update(title, text):
    cursor.execute("INSERT INTO updates(title, text, date) VALUES(?,?,datetime('now'))", (title, text))
    db.commit()

def get_updates():
    cursor.execute("SELECT * FROM updates ORDER BY id DESC")
    return cursor.fetchall()

def delete_update(update_id):
    cursor.execute("DELETE FROM updates WHERE id=?", (update_id,))
    db.commit()

# --- NEWS ---
def add_news(title, text, author=0):
    cursor.execute("INSERT INTO news(title, text, author, date) VALUES(?,?,?,datetime('now'))", (title, text, author))
    db.commit()

def get_news():
    cursor.execute("SELECT * FROM news ORDER BY id DESC")
    return cursor.fetchall()

def delete_news(news_id):
    cursor.execute("DELETE FROM news WHERE id=?", (news_id,))
    db.commit()

# --- SUPPORT, BUGS & SUGGESTIONS ---
def create_support(user_id, message):
    cursor.execute("INSERT INTO support(user_id, message, status, date) VALUES(?,?,?,datetime('now'))", (user_id, message, "open"))
    db.commit()

def get_support():
    cursor.execute("SELECT * FROM support ORDER BY id DESC")
    return cursor.fetchall()

def close_support(ticket_id):
    cursor.execute("UPDATE support SET status='closed' WHERE id=?", (ticket_id,))
    db.commit()

def add_bug(user_id, message):
    cursor.execute("INSERT INTO bugs(user_id, message, status, date) VALUES(?,?,?,datetime('now'))", (user_id, message, "new"))
    db.commit()

def get_bugs():
    cursor.execute("SELECT * FROM bugs ORDER BY id DESC")
    return cursor.fetchall()

def close_bug(bug_id):
    cursor.execute("UPDATE bugs SET status='closed' WHERE id=?", (bug_id,))
    db.commit()

def add_suggestion(user_id, message):
    cursor.execute("INSERT INTO suggestions(user_id, message, status, date) VALUES(?,?,?,datetime('now'))", (user_id, message, "new"))
    db.commit()

def get_suggestions():
    cursor.execute("SELECT * FROM suggestions ORDER BY id DESC")
    return cursor.fetchall()

def close_suggestion(suggestion_id):
    cursor.execute("UPDATE suggestions SET status='closed' WHERE id=?", (suggestion_id,))
    db.commit()

# --- STATS ---
def get_statistics():
    cursor.execute("SELECT COUNT(*) FROM users")
    users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM news")
    news = cursor.fetchone()[0]
    return users, news
