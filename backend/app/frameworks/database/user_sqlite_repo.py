import sqlite3
from app.interfaces.gateways.user_repository import UserRepository

class SQLiteUserRepository(UserRepository):
    def __init__(self, db_path="/data/example.db"):
        self.conn = sqlite3.connect(db_path)

    def insert(self, user):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email))
        self.conn.commit()
        return cur.lastrowid

    def fetch_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, email FROM users")
        return cur.fetchall()

    def delete(self, user_id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()
        return cur.rowcount
