class AuthUser:
    def __init__(self, username: str, password: str):
        if not username or not password:
            raise ValueError("Username and password are required")
        self.username = username
        self.password = password
