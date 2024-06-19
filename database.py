## chat gpt 사용해서 코드 작성
##database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 현재 파일의 디렉토리 경로를 가져옵니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 절대 경로를 사용하여 데이터베이스 파일 경로를 설정합니다.
SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR}/myapi.db" #직접 코드 작성

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
