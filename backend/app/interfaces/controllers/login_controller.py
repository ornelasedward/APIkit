from flask import request, jsonify
from app.use_cases.auth_user import AuthUseCase

def login_controller(secret_key):
    def inner():
        data = request.get_json()
        try:
            use_case = AuthUseCase(secret_key)
            token = use_case.execute(data["username"], data["password"])
            return jsonify({"token": token}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 403
    return inner
