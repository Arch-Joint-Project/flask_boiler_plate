from app.repositories import UserRepository

class UserController:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository


    def create(self, data):
        user = self.repository.create(data)
        return user
