from app.models.user import User
from app.database.sql_database import create_user, get_user

def create_new_user(user: User) -> User:
    return create_user(user)

def get_user_by_id(user_id: int) -> User:
    return get_user(user_id)