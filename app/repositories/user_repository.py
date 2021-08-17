from app.definitions.repository import SQLBaseRepository
from app.models import User

class UserRepository(SQLBaseRepository):
    model=User
