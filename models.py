from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from pydantic import BaseModel, EmailStr
from myapi.database import Base

Base = declarative_base()

# User 모델 정의
# User 모델 정의
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    token = Column(String, unique=True, index=True)
    #favorite_politicians = relationship("Politician", secondary="user_politicians", back_populates="users")

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
    attendance = Column(Integer)
    building = Column(Integer)   #재산 추가
    deposit = Column(Integer)
    car = Column(Integer)
    political_fund = Column(Integer)
    securities = Column(Integer)
    land = Column(Integer)
    #users = relationship("User", secondary="user_politicians", back_populates="favorite_politicians")

# 유저와 정치인 간의 관계를 위한 조인 테이블 정의
#user_politicians = Table(
#    'user_politicians', Base.metadata,
#    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
#    Column('politician_id', Integer, ForeignKey('politicians.id'), primary_key=True)
#)

# Pydantic 모델 정의
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    password_confirm: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    token: str

    class Config:
        orm_mode = True
