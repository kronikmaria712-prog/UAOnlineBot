import sqlite3

# Підключаємося до бази
db = sqlite3.connect("database.db")
cursor = db.cursor()

# Твій ID
my_id = 8214220798

# Додаємо в таблицю admins
try:
    cursor.execute(
        "INSERT INTO admins (user_id, rank, date_add) VALUES (?, ?, datetime('now'))",
        (my_id, "Owner")
    )
    db.commit()
    print(f"✅ Успіх! Користувача {my_id} додано як адміністратора.")
except sqlite3.IntegrityError:
    print("⚠️ Користувач уже є в списку адмінів.")

db.close()
