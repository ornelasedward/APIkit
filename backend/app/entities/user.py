class User:
    def __init__(self, name: str, email: str):
        if not name or not email:
            raise ValueError("Name and email are required")
        if "@" not in email:
            raise ValueError("Invalid email")
        self.name = name
        self.email = email
