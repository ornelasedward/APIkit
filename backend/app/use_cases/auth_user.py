import jwt
import datetime
from app.entities.auth_user import AuthUser

class AuthUseCase:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def execute(self, username, password):
        user = AuthUser(username, password)
        if user.username == "admin" and user.password == "password":
            return jwt.encode({
                'user': user.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, self.secret_key, algorithm="HS256")
        raise PermissionError("Invalid credentials")
