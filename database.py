import sqlite3

# ==========================================
# UA ONLINE MEDIA BOT 4.0 ULTIMATE
# DATABASE
# ==========================================

db = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = db.cursor()

# ==========================================
# USERS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER UNIQUE,

first_name TEXT,

last_name TEXT,

username TEXT,

language TEXT,

join_date TEXT,

last_activity TEXT

)
""")

# ==========================================
# ADMINS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS admins(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER UNIQUE,

rank TEXT,

date_add TEXT

)
""")

# ==========================================
# NEWS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS news(

id INTEGER PRIMARY KEY AUTOINCREMENT,

title TEXT,

text TEXT,

photo TEXT,

video TEXT,

author INTEGER,

date TEXT

)
""")

# ==========================================
# EVENTS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS events(

id INTEGER PRIMARY KEY AUTOINCREMENT,

title TEXT,

text TEXT,

date TEXT

)
""")

db.commit()

# ==========================================
# SUPPORT
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS support(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER,

message TEXT,

status TEXT,

date TEXT

)
""")

# ==========================================
# BUG REPORTS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS bugs(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER,

message TEXT,

status TEXT,

date TEXT

)
""")

# ==========================================
# SUGGESTIONS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS suggestions(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER,

message TEXT,

status TEXT,

date TEXT

)
""")

# ==========================================
# UPDATES
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS updates(

id INTEGER PRIMARY KEY AUTOINCREMENT,

title TEXT,

text TEXT,

date TEXT

)
""")

# ==========================================
# LOGS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER,

action TEXT,

date TEXT

)
""")

# ==========================================
# STATISTICS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS statistics(

id INTEGER PRIMARY KEY AUTOINCREMENT,

users INTEGER,

news INTEGER,

events INTEGER,

updates INTEGER,

date TEXT

)
""")

db.commit()

# ==========================================
# FUNCTIONS
# ==========================================

def add_user(user):
    cursor.execute(
        """
        INSERT OR IGNORE INTO users(
            user_id,
            first_name,
            last_name,
            username,
            language,
            join_date,
            last_activity
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            user.id,
            user.first_name,
            user.last_name,
            user.username,
            user.language_code,
            "",
            ""
        )
    )
    db.commit()


def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


# ==========================================
# NEWS
# ==========================================

def add_news(title, text, photo=None, video=None, author=0):
    cursor.execute(
        """
        INSERT INTO news(
            title,
            text,
            photo,
            video,
            author,
            date
        )
        VALUES(?,?,?,?,?,datetime('now'))
        """,
        (
            title,
            text,
            photo,
            video,
            author
        )
    )
    db.commit()


def get_news():
    cursor.execute(
        "SELECT * FROM news ORDER BY id DESC"
    )
    return cursor.fetchall()


def delete_news(news_id):
    cursor.execute(
        "DELETE FROM news WHERE id=?",
        (news_id,)
    )
    db.commit()


# ==========================================
# ADMINS
# ==========================================

def add_admin(user_id, rank):
    cursor.execute(
        """
        INSERT OR IGNORE INTO admins(
            user_id,
            rank,
            date_add
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            user_id,
            rank
        )
    )
    db.commit()


def get_admins():
    cursor.execute("SELECT * FROM admins")
    return cursor.fetchall()


# ==========================================
# DATABASE SAVE
# ==========================================

db.commit()

print("✅ Database успішно завантажена.")

# ==========================================
# FUNCTIONS
# ==========================================

def add_user(user):
    cursor.execute(
        """
        INSERT OR IGNORE INTO users(
            user_id,
            first_name,
            last_name,
            username,
            language,
            join_date,
            last_activity
        )
        VALUES(?,?,?,?,?,datetime('now'),datetime('now'))
        """,
        (
            user.id,
            user.first_name or "",
            user.last_name or "",
            user.username or "",
            user.language_code or ""
        )
    )
    db.commit()


def update_activity(user_id):
    cursor.execute(
        """
        UPDATE users
        SET last_activity=datetime('now')
        WHERE user_id=?
        """,
        (user_id,)
    )
    db.commit()


def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
    
    # ==========================================
# NEWS FUNCTIONS
# ==========================================


def add_news(title, text, photo=None, video=None, author=0):
    cursor.execute(
        """
        INSERT INTO news(
            title,
            text,
            photo,
            video,
            author,
            date
        )
        VALUES(?,?,?,?,?,datetime('now'))
        """,
        (
            title,
            text,
            photo,
            video,
            author
        )
    )
    db.commit()


def get_news():
    cursor.execute(
        """
        SELECT *
        FROM news
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


def get_news_by_id(news_id):
    cursor.execute(
        """
        SELECT *
        FROM news
        WHERE id=?
        """,
        (news_id,)
    )

    return cursor.fetchone()


def delete_news(news_id):
    cursor.execute(
        """
        DELETE FROM news
        WHERE id=?
        """,
        (news_id,)
    )

    db.commit()
    
    # ==========================================
# ADMIN FUNCTIONS
# ==========================================


def add_admin(user_id, rank="Admin"):
    cursor.execute(
        """
        INSERT OR IGNORE INTO admins(
            user_id,
            rank,
            date_add
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            user_id,
            rank
        )
    )

    db.commit()


def remove_admin(user_id):
    cursor.execute(
        """
        DELETE FROM admins
        WHERE user_id=?
        """,
        (user_id,)
    )

    db.commit()


def is_admin(user_id):
    cursor.execute(
        """
        SELECT user_id
        FROM admins
        WHERE user_id=?
        """,
        (user_id,)
    )

    return cursor.fetchone() is not None


def get_admins():
    cursor.execute(
        """
        SELECT *
        FROM admins
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()
    
    # ==========================================
# SUPPORT FUNCTIONS
# ==========================================


def create_support(user_id, message):
    cursor.execute(
        """
        INSERT INTO support(
            user_id,
            message,
            status,
            date
        )
        VALUES(?,?,?,datetime('now'))
        """,
        (
            user_id,
            message,
            "open"
        )
    )

    db.commit()


def get_support():
    cursor.execute(
        """
        SELECT *
        FROM support
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


def close_support(ticket_id):
    cursor.execute(
        """
        UPDATE support
        SET status='closed'
        WHERE id=?
        """,
        (ticket_id,)
    )

    db.commit()


def delete_support(ticket_id):
    cursor.execute(
        """
        DELETE FROM support
        WHERE id=?
        """,
        (ticket_id,)
    )

    db.commit()
    
    # ==========================================
# BUGS FUNCTIONS
# ==========================================


def add_bug(user_id, message):
    cursor.execute(
        """
        INSERT INTO bugs(
            user_id,
            message,
            status,
            date
        )
        VALUES(?,?,?,datetime('now'))
        """,
        (
            user_id,
            message,
            "new"
        )
    )

    db.commit()


def get_bugs():
    cursor.execute(
        """
        SELECT *
        FROM bugs
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


def update_bug_status(bug_id, status):
    cursor.execute(
        """
        UPDATE bugs
        SET status=?
        WHERE id=?
        """,
        (
            status,
            bug_id
        )
    )

    db.commit()


def delete_bug(bug_id):
    cursor.execute(
        """
        DELETE FROM bugs
        WHERE id=?
        """,
        (bug_id,)
    )

    db.commit()
    
    # ==========================================
# SUGGESTIONS FUNCTIONS
# ==========================================


def add_suggestion(user_id, message):
    cursor.execute(
        """
        INSERT INTO suggestions(
            user_id,
            message,
            status,
            date
        )
        VALUES(?,?,?,datetime('now'))
        """,
        (
            user_id,
            message,
            "new"
        )
    )

    db.commit()


def get_suggestions():
    cursor.execute(
        """
        SELECT *
        FROM suggestions
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


def update_suggestion_status(suggestion_id, status):
    cursor.execute(
        """
        UPDATE suggestions
        SET status=?
        WHERE id=?
        """,
        (
            status,
            suggestion_id
        )
    )

    db.commit()


def delete_suggestion(suggestion_id):
    cursor.execute(
        """
        DELETE FROM suggestions
        WHERE id=?
        """,
        (suggestion_id,)
    )

    db.commit()
    
    # ==========================================
# UPDATES FUNCTIONS
# ==========================================


def add_update(title, text):
    cursor.execute(
        """
        INSERT INTO updates(
            title,
            text,
            date
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            title,
            text
        )
    )

    db.commit()


def get_updates():
    cursor.execute(
        """
        SELECT *
        FROM updates
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


# ==========================================
# LOGS FUNCTIONS
# ==========================================


def add_log(user_id, action):
    cursor.execute(
        """
        INSERT INTO logs(
            user_id,
            action,
            date
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            user_id,
            action
        )
    )

    db.commit()


def get_logs():
    cursor.execute(
        """
        SELECT *
        FROM logs
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


# ==========================================
# STATISTICS FUNCTIONS
# ==========================================


def get_statistics():

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )
    users = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM news"
    )
    news_count = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM events"
    )
    events_count = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM updates"
    )
    updates_count = cursor.fetchone()[0]


    return {
        "users": users,
        "news": news_count,
        "events": events_count,
        "updates": updates_count
    }


# ==========================================
# DATABASE READY
# ==========================================

db.commit()

print("✅ UA ONLINE MEDIA BOT 4.0 DATABASE READY")

# ==========================================
# EVENTS FUNCTIONS
# ==========================================


def add_event(title, text):

    cursor.execute(
        """
        INSERT INTO events(
            title,
            text,
            date
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            title,
            text
        )
    )

    db.commit()



def get_events():

    cursor.execute(
        """
        SELECT *
        FROM events
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()



def delete_event(event_id):

    cursor.execute(
        """
        DELETE FROM events
        WHERE id=?
        """,
        (event_id,)
    )

    db.commit()
    
    # ==========================================
# EXTRA DATABASE FUNCTIONS
# ==========================================


# ---------- ADMINS ----------

def is_admin(user_id):

    cursor.execute(
        "SELECT * FROM admins WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone() is not None



# ---------- USERS ----------

def get_users():

    cursor.execute(
        "SELECT * FROM users"
    )

    return cursor.fetchall()



def get_user(user_id):

    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone()



# ---------- LOGS ----------

def add_log(user_id, action):

    cursor.execute(
        """
        INSERT INTO logs(
            user_id,
            action,
            date
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            user_id,
            action
        )
    )

    db.commit()



def get_logs():

    cursor.execute(
        """
        SELECT *
        FROM logs
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()



# ---------- UPDATES ----------

def add_update(title, text):

    cursor.execute(
        """
        INSERT INTO updates(
            title,
            text,
            date
        )
        VALUES(?,?,datetime('now'))
        """,
        (
            title,
            text
        )
    )

    db.commit()



def get_updates():

    cursor.execute(
        "SELECT * FROM updates ORDER BY id DESC"
    )

    return cursor.fetchall()



def delete_update(update_id):

    cursor.execute(
        "DELETE FROM updates WHERE id=?",
        (update_id,)
    )

    db.commit()



# ---------- BUGS ----------

def add_bug(user_id, message):

    cursor.execute(
        """
        INSERT INTO bugs(
            user_id,
            message,
            status,
            date
        )
        VALUES(?,?,?,datetime('now'))
        """,
        (
            user_id,
            message,
            "open"
        )
    )

    db.commit()



def get_bugs():

    cursor.execute(
        "SELECT * FROM bugs ORDER BY id DESC"
    )

    return cursor.fetchall()



def close_bug(bug_id):

    cursor.execute(
        """
        UPDATE bugs
        SET status='closed'
        WHERE id=?
        """,
        (bug_id,)
    )

    db.commit()



# ---------- SUGGESTIONS ----------

def add_suggestion(user_id, message):

    cursor.execute(
        """
        INSERT INTO suggestions(
            user_id,
            message,
            status,
            date
        )
        VALUES(?,?,?,datetime('now'))
        """,
        (
            user_id,
            message,
            "open"
        )
    )

    db.commit()



def get_suggestions():

    cursor.execute(
        "SELECT * FROM suggestions ORDER BY id DESC"
    )

    return cursor.fetchall()



def close_suggestion(suggestion_id):

    cursor.execute(
        """
        UPDATE suggestions
        SET status='closed'
        WHERE id=?
        """,
        (suggestion_id,)
    )

    db.commit()
    
    
    