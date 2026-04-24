import sqlite3

conn = sqlite3.connect("chatbot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT,
    response TEXT
)
""")

def save_log(query, response):
    cursor.execute("INSERT INTO logs (query, response) VALUES (?, ?)", (query, response))
    conn.commit()