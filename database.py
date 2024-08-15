import sqlite3

def init_db():
    conn = sqlite3.connect('neetechs_bot.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            is_authenticated BOOLEAN NOT NULL CHECK (is_authenticated IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect('neetechs_bot.db')
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO users (user_id, is_authenticated) VALUES (?, 0)', (user_id,))
    conn.commit()
    conn.close()

def authenticate_user(user_id):
    conn = sqlite3.connect('neetechs_bot.db')
    c = conn.cursor()
    c.execute('UPDATE users SET is_authenticated = 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

def is_user_authenticated(user_id):
    conn = sqlite3.connect('neetechs_bot.db')
    c = conn.cursor()
    c.execute('SELECT is_authenticated FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] == 1 if result else False
