import sqlite3
from app.use_cases.insert_user import InsertUserUseCase
from app.frameworks.database.user_sqlite_repo import SQLiteUserRepository

def test_insert_user(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.commit()

    repo = SQLiteUserRepository(str(db_path))
    usecase = InsertUserUseCase(repo)
    row_id = usecase.execute("Bob", "bob@example.com")

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (row_id,))
    row = cur.fetchone()
    assert row[1] == "Bob"
    assert row[2] == "bob@example.com"
