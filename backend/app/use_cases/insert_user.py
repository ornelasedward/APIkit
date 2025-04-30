from app.entities.user import User

class InsertUserUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, name: str, email: str):
        user = User(name, email)
        return self.user_repo.insert(user)
