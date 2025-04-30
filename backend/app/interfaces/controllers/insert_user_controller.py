from flask import request, jsonify
from app.use_cases.insert_user import InsertUserUseCase
from app.frameworks.database.user_sqlite_repo import SQLiteUserRepository

def insert_user_controller():
    data = request.get_json()
    try:
        use_case = InsertUserUseCase(SQLiteUserRepository())
        row_id = use_case.execute(data["name"], data["email"])
        return jsonify({"inserted_id": row_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
