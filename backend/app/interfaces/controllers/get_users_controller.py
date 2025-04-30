from flask import jsonify
from app.use_cases.get_users import GetUsersUseCase
from app.frameworks.database.user_sqlite_repo import SQLiteUserRepository

def get_users_controller():
    try:
        use_case = GetUsersUseCase(SQLiteUserRepository())
        users = use_case.execute()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
