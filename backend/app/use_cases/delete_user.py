class DeleteUserUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id: int):
        return self.user_repo.delete(user_id)
