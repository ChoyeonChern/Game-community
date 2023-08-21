from sqlmodel import Session, SQLModel, create_engine
from app.models.user import User

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_user(user: User) -> User:
    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def get_user(user_id: int) -> User:
    with get_session() as session:
        user = session.get(User, user_id)
    return user
