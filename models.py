from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Text, Table, ForeignKey  # Table과 ForeignKey를 import합니다.
from sqlalchemy.orm import relationship
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
    favorite_politicians = Column(Text, nullable=True)  # 추가된 부분

    # 관계 설정
    politicians = relationship("Politician", secondary="user_politicians", back_populates="users")


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
    # 관계 설정
    users = relationship("User", secondary="user_politicians", back_populates="politicians")


# 유저와 정치인 간의 관계를 위한 테이블 정의
user_politicians = Table(
    'user_politicians', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('politician_id', Integer, ForeignKey('politicians.id'))
)