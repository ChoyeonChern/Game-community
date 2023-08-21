from sqlmodel import Session, select
from app.database.sql_database import engine
from app.models.user import User


def create_user(username: str, email: str, password: str) -> User:
    user = User(username=username, email=email, password=password)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def get_user(user_id: int) -> User:
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        result = session.exec(statement)
        user = result.one()
    return user
