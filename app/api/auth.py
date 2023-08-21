from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPBasicCredentials
from sqlalchemy import select

from app.database.sql_database import get_session
from app.models.user import User
from app.utils.auth import create_access_token, verify_password, get_password_hash

router = APIRouter()

security = HTTPBearer()


def get_user_by_username(username: str) -> User:
    with get_session() as session:
        user = session.exec(select(User).where(User.username == username)).first()
    return user


@router.post("/login")
def login(credentials: HTTPBasicCredentials):
    # 获取用户名和密码
    username = credentials.username
    password = credentials.password

    # 在这里进行用户登录验证
    # 假设我们有一个名为`get_user_by_username`的函数来获取用户信息
    user = get_user_by_username(username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # 生成JWT令牌
    access_token = create_access_token({"sub": user.username})

    # 返回JWT令牌
    return {"access_token": access_token}
