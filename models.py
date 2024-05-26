from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from myapi.database import Base
import secrets

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    token = Column(String, unique=True, index=True)

class UserIn(BaseModel):
    username: str
    email: str
    password: str
    password_confirm: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    token: str

    class Config:
        orm_mode = True

# Politician 모델 정의
class Politician(Base):
    __tablename__ = 'politicians'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    party = Column(String)
    constituency = Column(String)
    contact = Column(String)
    gender = Column(String)
    election_count = Column(String)
    election_method = Column(String)
    attendance = Column(Integer)  # 출석을 나타내는 정수형 열 추가