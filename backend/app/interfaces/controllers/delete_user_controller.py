from flask import request, jsonify
from app.use_cases.delete_user import DeleteUserUseCase
from app.frameworks.database.user_sqlite_repo import SQLiteUserRepository

def delete_user_controller():
    try:
        user_id = request.args.get("id")
        use_case = DeleteUserUseCase(SQLiteUserRepository())
        count = use_case.execute(int(user_id))
        return jsonify({"deleted": count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
