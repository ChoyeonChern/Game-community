from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

# 根据您的数据库配置，替换以下字符串
database_url = "sqlite:///./mydatabase.db"

# 创建数据库引擎
engine = create_engine(database_url)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 创建基本模型类
class MyBase(SQLModel):
    class Config:
        orm_mode = True
