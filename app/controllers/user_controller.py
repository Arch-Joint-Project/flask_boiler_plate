from app.repositories import UserRepository

class UserController:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository


    def create(self, data):
        user = self.repository.create(data)
        return user


    # read_by_id
    def read_by_id(self,obj_id):
        user = self.repository.find_by_id(obj_id)
        return user

    # read all
    def read_all(self,data):
        user = self.repository.find_all(data)
        return user

    # update_by_id
    def update_by_id(self, obj_id,obj_in):
        user = self.repository.update_by_id(obj_id,obj_in)
        return user

    # update_all
    def update_all(self,query_info, obj_in):
        user = self.repository.update(query_info,obj_in)
        return user

    # delete
    def delete(self,obj_id):
        user = self.repository.delete(obj_id)
        return user

